import pandas as pd
from columns import columns
from company_scraper import fetch_companies


companies = [] # all company data


if __name__ == "__main__":
    # fetch companies by industry
    companies.extend(fetch_companies("tech", "tech", "Technology", 1, 2))
    # companies.extend(fetch_companies("pharmaceuticals", "pharmaceutical", "Pharmaceuticals", 1, 2))
    # companies.extend(fetch_companies("real-estate", "real-estate", "Real Estate", 1, 2))
    # companies.extend(fetch_companies("oil-gas", "oil-and-gas", "Oil&Gas", 1, 2))
    # companies.extend(fetch_companies("retail", "retail", "Retail", 1, 2))
    # companies.extend(fetch_companies("insurance", "insurance", "Insurance", 1, 2))
    # companies.extend(fetch_companies("food", "food", "Food", 1, 2))
    # companies.extend(fetch_companies("electricity", "electricity", "Electricity", 1, 2))
    # convert pandas to csv and save
    df = pd.DataFrame(data=companies, columns=columns)
    df.to_csv("companies/companies_data.csv", index=False)