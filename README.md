# Tableau Industry Insights Dashboard

## Problem Statement
A comprehensive financial analysis [dashboard](google.com) comparing the financial performance and key metrics of **1500** companies across **8** different industries. Utilizing the financial information from [companiesmarketcap.com](https://companiesmarketcap.com/) the dashboard offers a wide range of visualizations and metrics, including:

1. point 1
2. point 2

You can visit the public dashboard [here](google.com)

## Findings and Observations from the [Dashboard](google.com)
1. finding 1
2. finding 2

## Build from Source
1. Clone the repo
```bash
git clone https://github.com/zzarif/Tableau-Industry-Insights-Dashboard.git
```
2. Initialize and activate virtual environment
```bash
virtualenv --no-site-packages venv
source venv/Scripts/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
*Note: Select virtual environment interpreter from* ```Ctrl```+```Shift```+```P```
## Run the Selenium Scraper
```bash
python companies/main.py
```
At this stage, you will get a file named [companies_data.csv](https://github.com/zzarif/Tableau-Industry-Insights-Dashboard/blob/main/companies/companies_data.csv) (this file requires data transformation and cleaning)

## Transform and Clean the data
```bash
python companies/transform_data.py
```
At this stage, you will get a file named [transformed_companies_data.csv](https://github.com/zzarif/Tableau-Industry-Insights-Dashboard/blob/main/companies/transformed_companies_data.csv) (load this file into Tableau)