from selenium import webdriver
from selenium.webdriver.common.by import By
from html_row_to_dict import get_dict_from_html_row
from urls import TECH_ENDPOINT, metric_endpoints
from columns import columns


PAGE_COUNT = 2


def tech_scraper():
    for page_id in range(1,PAGE_COUNT):
        driver = webdriver.Chrome()
        driver.get(f"{TECH_ENDPOINT}?page={page_id}")

        print(f"======[START] Fetching 100 items from page {page_id}")
        table_body = driver.find_element(By.TAG_NAME, "tbody")
        table_rows = table_body.find_elements(By.CSS_SELECTOR, "tr:not(.ad-tr.no-sort)")

        tech_companies = [ get_dict_from_html_row(row, "Technology") for row in table_rows ]
        
        print("======[END]")
        driver.quit()

        for company in tech_companies[0:2]:
            for metric in metric_endpoints:
                driver = webdriver.Chrome()
                driver.get(f"{company.get(columns[1])}/{metric}")

                print(f"======[START] Fetching {company.get(columns[0])}'s {metric}")
                metric_val = driver.find_element(By.CLASS_NAME, "background-ya").text
                company[metric] = metric_val

                print("======[END]")
                driver.quit()

        
        print(len(tech_companies))
        print(tech_companies[0:2])

        ###