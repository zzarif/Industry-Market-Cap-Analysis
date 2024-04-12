from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from html_row_to_dict import get_dict_from_html_row
from urls import BASE_URL, metric_endpoints
from columns import columns


PAGE_COUNT = 3 # will fetch (count-1)*100 companies


# scrape and fetch the companies
def fetch_companies(industry_seg, industry_subseg, label):
    for page_id in range(1,PAGE_COUNT):
        driver = webdriver.Chrome()
        driver.get(f"{BASE_URL}/{industry_seg}/largest-{industry_subseg}-companies-by-number-of-employees/?page={page_id}")

        print(f"======[START] Fetching 100 items from page {page_id}")
        table_body = driver.find_element(By.TAG_NAME, "tbody")
        table_rows = table_body.find_elements(By.CSS_SELECTOR, "tr:not(.ad-tr.no-sort)")

        fetched_companies = [ get_dict_from_html_row(row, label) for row in table_rows ]
        
        print("======[END]")
        driver.quit()

        # fetch all metrics for the companies
        for idx, company in enumerate(fetched_companies):
            for metric in metric_endpoints:
                driver = webdriver.Chrome()
                driver.get(f"{company.get(columns[1])}/{metric}")

                print(f"======[START] Fetching {idx}-{company.get(columns[0])}'s {metric}")
                try: 
                    company[metric] = driver.find_element(By.CLASS_NAME, "background-ya").text
                except NoSuchElementException:
                    company[metric] = ""

                print("======[END]")
                driver.quit()

        return fetched_companies