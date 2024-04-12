BASE_URL = "https://companiesmarketcap.com" # base url

# tech endpoint
TECH_ENDPOINT = f"{BASE_URL}/tech/largest-tech-companies-by-number-of-employees/"
# pharma endpoint
PHARMA_ENDPOINT = f"{BASE_URL}/pharmaceuticals/largest-pharmaceutical-companies-by-number-of-employees/"
# real estate endpoint
REAL_ESTATE_ENDPOINT = f"{BASE_URL}/real-estate/largest-real-estate-companies-by-number-of-employees/"

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


### finance ~1K (not compatible)
### oil and gas 360
### retail 300
### insurance 250
### food 250
### electricity company 250
### telecom 200
### construction 100