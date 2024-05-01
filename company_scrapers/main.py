import pandas as pd
from columns import columns
from company_scraper import fetch_companies


companies = [] # all company data


if __name__ == "__main__":
    # fetch companies by industry
    companies.extend(fetch_companies("tech", "tech", "Technology"))
    companies.extend(fetch_companies("pharmaceuticals", "pharmaceutical", "Pharmaceuticals"))
    companies.extend(fetch_companies("real-estate", "real-estate", "Real Estate"))
    companies.extend(fetch_companies("oil-gas", "oil-and-gas", "Oil&Gas"))
    companies.extend(fetch_companies("retail", "retail", "Retail"))
    companies.extend(fetch_companies("insurance", "insurance", "Insurance"))
    companies.extend(fetch_companies("food", "food", "Food"))
    companies.extend(fetch_companies("electricity", "electricity", "Electricity"))
    # convert pandas to csv and save
    df = pd.DataFrame(data=companies, columns=columns)
    df.to_csv("company_data/companies_data.csv", index=False)