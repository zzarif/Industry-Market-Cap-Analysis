from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from html_row_to_dict import get_dict_from_html_row
from urls import BASE_URL, metric_endpoints
from columns import columns
import time


# scrape and fetch the companies
def fetch_companies(industry_seg, industry_subseg, label, page=1, max_page=2):
    """
    Parameters:
        - industry_seg: First segment of URL slug for a particular industry.
        - industry_subseg: Second segment of URL slug for a particular industry.
        - label: Label for a particular industry.
        - page: scraper will start from this page.
        - max_page: scraper will stop at this page.

    Returns:
        - fetched_companies: The list of all the companies and their data for a particular industry.
    """
    start = time.time()
    fetched_companies = [] # list containing all companies

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless") # run in background
    chrome_options.add_argument("--window-size=1920,1080") # render full screen
    chrome_options.add_argument('log-level=3') # suppress verbose log messages

    for page_id in range(page, max_page+1):
        driver = webdriver.Chrome(options=chrome_options) # initialize driver
        driver.get(f"{BASE_URL}/{industry_seg}/largest-{industry_subseg}-companies-by-number-of-employees/?page={page_id}")

        print(f"======[START] Fetching 100 items from page {page_id}")
        table_body = driver.find_element(By.TAG_NAME, "tbody")
        table_rows = table_body.find_elements(By.CSS_SELECTOR, "tr:not(.ad-tr.no-sort)")

        current_fetched_companies = [ get_dict_from_html_row(row, label) for row in table_rows ]
        fetched_companies.extend(current_fetched_companies)
        
        print("======[END]")
        driver.quit()

        # fetch all metrics for the companies
        for idx, company in enumerate(current_fetched_companies):
            for metric in metric_endpoints:
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(f"{company.get(columns[1])}/{metric}")

                print(f"======[START] Fetching {idx}-{company.get(columns[0])}'s {metric}")
                try: 
                    company[metric] = driver.find_element(By.CLASS_NAME, "background-ya").text
                except NoSuchElementException:
                    company[metric] = ""

                print("======[END]")
                driver.quit()

    print(f"Time taken: {time.time() - start}")
    return fetched_companies