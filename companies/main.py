import pandas as pd
from columns import columns
from tech_scraper import fetch_tech_companies
from pharma_scraper import fetch_pharma_companies
from real_estate_scraper import fetch_real_estate_companies


companies = [] # all company data


if __name__ == "__main__":
    companies.extend(fetch_tech_companies())
    companies.extend(fetch_pharma_companies())
    companies.extend(fetch_real_estate_companies())
    df = pd.DataFrame(data=companies, columns=columns)
    df.to_csv("companies_data.csv", index=False)