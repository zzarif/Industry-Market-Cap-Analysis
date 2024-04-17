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
*Note: Select virtual environment interpreter from* `Ctrl`+`Shift`+`P`
## Run the Selenium Scraper
### Traditional Approach
```bash
python companies/main.py
```
Run this command and wait for it to finish. When complete, you will get a file named [companies_data.csv](companies/companies_data.csv) (this file requires data transformation in the next step)

### Alternative Approach (Scraping Parallelly)
Using traditional approach, scraping financial data for 1500 companies one-by-one might take a significant amount of time (several hours) depending on your network bandwidth. A better and faster approach would be to split the task into multiple scraper instances that will scrape data parallely. Each scraper will be assigned to scrape financial data of the companies belonging to a particular industry.

To do this, you can simply create 8 copies of the `main.py` file (for 8 industries) and modify each `main.py` to fetch companies only for a particular industry. Now, run all the copies parallelly and merge the output CSV files.

Alternatively, you can use Python's `multiprocessing` module to spawn multiple processes to accomplish the same task.

Be sure to rename the final merged CSV file as [companies_data.csv](companies/companies_data.csv) (this file requires data transformation in the next step)

## Transform and Clean the data
```bash
python companies/transform_data.py
```
At this stage, you will get a file named [transformed_companies_data.csv](companies/transformed_companies_data.csv) (you can load this file into Tableau as Text file)