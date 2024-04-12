BASE_URL = "https://companiesmarketcap.com" # base url

### tech enpoints
TECH_MARKET_CAP_ENDPOINT = f"{BASE_URL}/tech/largest-tech-companies-by-market-cap/"
TECH_REVENUE_ENDPOINT = f"{BASE_URL}/tech/largest-tech-companies-by-revenue/"
TECH_EARNINGS_ENDPOINT = f"{BASE_URL}/tech/most-profitable-tech-companies/"
TECH_PE_RATIO_ENDPOINT = f"{BASE_URL}/tech/tech-companies-ranked-by-pe-ratio/"
TECH_OPERATING_MARGIN_ENDPOINT = f"{BASE_URL}/tech/tech-companies-ranked-by-operating-margin/"

TECH_ENDPOINT = f"{BASE_URL}/tech/largest-tech-companies-by-number-of-employees/"

metric_endpoints = [
    "marketcap",
    "revenue",
    "earnings",
    "operating-margin",
    "total-assets",
    "total-liabilities",
    "total-debt",
    "net-assets",
    "pe-ratio",
    "ps-ratio"
]


### pharma endpoints
# PHARMA = f"{BASE_URL}/pharmaceuticals"
# PHARMA_MARKET_CAP_ENDPOINT = f"{PHARMA}/largest-pharmaceutical-companies-by-market-cap"
# PHARMA_EMPLOYEES_ENDPOINT = f"{PHARMA}/largest-pharmaceutical-companies-by-number-of-employees"

# ### real estate endpoints
# REAL_ESTATE = f"{BASE_URL}/real-estate"
# REAL_ESTATE_MARKET_CAP_ENDPOINT = f"{REAL_ESTATE}/largest-real-estate-companies-by-market-cap"
# REAL_ESTATE_EMPLOYEES_ENDPOINT = f"{REAL_ESTATE}/largest-real-estate-companies-by-number-of-employees"



### finance ~1K (not compatible)
### oil and gas 360
### retail 300
### insurance 250
### food 250
### electricity company 250
### telecom 200
### construction 100