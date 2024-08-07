<h1 align="center">
  <br>
  <!-- <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.png" alt="Markdownify" width="200"></a>
  <br> -->
  Industry Market Cap Analysis
  <br>
</h1>

<h4 align="center">Financial analysis dashboards comparing 1500 companies across 8 industries.</h4>

<p align="center">
  <!-- <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a> -->
  <!-- <a href="">
      <img src="https://img.shields.io/badge/website-online-blue.svg">
  </a> -->
  <a href="https://github.com/zzarif/Industry-Market-Cap-Analysis">
    <img src="https://img.shields.io/github/last-commit/zzarif/Industry-Market-Cap-Analysis">
  </a>
  <a href="https://www.kaggle.com/datasets/zibranzarif/industry-market-cap-analysis-dataset">
    <img src="https://img.shields.io/badge/dataset-kaggle-blue.svg">
  </a>
  <a href="https://public.tableau.com/app/profile/zibran.zarif/viz/IndustryInsightsDashboard/IndustryComparisonDashboard">
    <img src="https://img.shields.io/badge/tableau-public-red.svg">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-yellow.svg">
  </a>

</p>

<p align="center">
  <a href="#-problem-statement">Problem Statement</a> •
  <a href="#findings-and-observations-from-the-dashboards">Findings from Dashboards</a> •
  <a href="#%EF%B8%8F-build-from-source">Build from Source</a> •
  <a href="#-run-the-selenium-scraper">Run the Selenium Scraper</a> •
  <a href="#-transform-and-clean-the-data">Transform and Clean the data</a> •
  <a href="#%EF%B8%8F-contact">Contact</a>
</p>

## 📋 Problem Statement
Comprehensive financial analysis [dashboards](https://public.tableau.com/app/profile/zibran.zarif/viz/IndustryInsightsDashboard/IndustryComparisonDashboard) comparing the financial performance and key metrics of **1500** companies across **8** different industries. Utilizing the financial information from [companiesmarketcap.com](https://companiesmarketcap.com/) the dashboard offers a wide range of visualizations and metrics, including:

1. Bar charts comparing the average market cap, revenue, and earnings of companies in each industry.
2. Employee productivity scatter plots presenting Revenue-per-Employee and Earnings-per-Employee color coded by industry.
3. Geographic distribution of market capital and companies.
4. Comparative Price-to-Sales and Price-to-Earning Ratio identifying growth-oriented industries.
5. Box plots revealing the typical range and variability of operating margins of companies in each industry.
6. Debt-to-Equity and Current Ratio heatmaps showing financial health of companies.

Here are the links to Tableau public dashboards:
- [Industry Comparison Dashboard](https://public.tableau.com/app/profile/zibran.zarif/viz/IndustryInsightsDashboard/IndustryComparisonDashboard)
- [Geographical Distribution and Operating Margin Dashboard](https://public.tableau.com/app/profile/zibran.zarif/viz/IndustryInsightsDashboard/GeographicDistributionandOperatingMarginDashboard)
- [Financial Health Heatmaps Dashboard](https://public.tableau.com/app/profile/zibran.zarif/viz/IndustryInsightsDashboard/FinancialHealthDashboard)

## Findings and Observations from the [Dashboards](https://public.tableau.com/app/profile/zibran.zarif/viz/IndustryInsightsDashboard/IndustryComparisonDashboard)

### 📊 [Dashboard 1:](https://public.tableau.com/app/profile/zibran.zarif/viz/IndustryInsightsDashboard/IndustryComparisonDashboard) Industry Comparison
![industry_comparison_dashboard](dashboard/images/industry_comparison_dashboard.png)
Findings:
1. **Tehnology** has the highest average market value in general and **Real Estate** is the lowest. However, **Oil & Gas** is the leading industry in terms of total country-wise average market cap. **Saudi Arabia** is the largest contributor.
2. **Oil & Gas** industry dominates the market in terms of Average Revenue and Earnings. **Real Estate** is the lowest.
3. In terms of Revenue per employee, **Saudi Aramco** (Oil & Gas) is the highest whereas **Phoenix Group** (Insurance) is the lowest. 
4. In terms of Earnings per employee, again **Saudi Aramco** (Oil & Gas) is the highest whereas **Walgreens Boots Alliance** (Pharmaceuticals) is the lowest. On average, **Oil & Gas** is the most employee productive industry.

### 📊 [Dashboard 2:](https://public.tableau.com/app/profile/zibran.zarif/viz/IndustryInsightsDashboard/GeographicDistributionandOperatingMarginDashboard) Geographical Distribution and Operating Margin
![geographical_dist_and_operating_margin_dashboard](dashboard/images/geographical_dist_and_operating_margin_dashboard.png)
Findings:
1. **Saudi Arabia** has the largest share of market capital ($248.3T), followed by **USA** ($56.4T), and **Denmark** ($51.6T)
2. From the 1500 total companies, 591 belong to **USA** alone, followed by **India** (96), **China** (67), and **Hong Kong** (48)
3. **Real Estate** has the highest median operating margin at around 15.4%, followed by **Oil & Gas** and **Pharmaceuticals** both at approximately 11.1%. This suggests these industries tend to have healthier operating profitability on average.
4. The **Pharmaceuticals** industry has the widest spread between its upper and lower whiskers, indicating it has the most variability in operating margins. Companies span a wide range from highly profitable to unprofitable.
5. Insurance, Oil & Gas, and Real Estate have their entire boxes above the zero line, meaning **over 75%** of companies have positive margins. In contrast, **Pharmaceuticals** and **Food** have a large portion of their boxes below zero, indicating a significant number of unprofitable companies.
6. **Technology** companies tend to have both high P/S and high P/E ratios compared to other industries. It is a growth-oriented sector.
7. **Retail** and **Food** industries generally have lower P/S and P/E ratios. These are slower-growth sectors.

### 📊 [Dashboard 3:](https://public.tableau.com/app/profile/zibran.zarif/viz/IndustryInsightsDashboard/FinancialHealthDashboard) Financial Health Heatmaps Dashboard
![financial_health_dashboard](dashboard/images/financial_health_dashboard.png)
Findings:
1. **Real Estate** companies from the **UK** have the most average Debt. Same goes for **Pharmaceuticals** (Canada), **Retail** (Saudi Arabia), and **Insurance** (Japan).
2. **Food** companies in **Malaysia** have significantly more total assets relative to its total liabilities. Same goes for **Oil & Gas** (Russia), and **Retail** (Greece).

## ⚙️ Build from Source
1. Clone the repo
```bash
git clone https://github.com/zzarif/Industry-Market-Cap-Analysis.git
cd Industry-Market-Cap-Analysis/
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
## 🌐 Run the Selenium Scraper
### Traditional Approach
```bash
python scraper/main.py
```
Run this command and wait for it to finish. When complete, you will get a file named [scraped_company_data.csv](data/scraped_company_data.csv) (this file requires data transformation in the next step).

#### How the scraping is done:
The `main.py` file calls `fetch_companies` method 8 times for 8 different industries. Each time `fetch_companies` method fetches 200 companies' data for each industry (100 companies for *Electricity* industry) totalling to 1500 companies' data. `fetch_companies` method uses `selenium` webdriver to scrape [companiesmarketcap.com](https://companiesmarketcap.com/) with necessary `chrome_options` added as arguments. At a time, it will iterate over maximum 2 pages to scrape 200 companies' data (each page has 100 companies listed). During each iteration, the outer `for` loop, fetches 100 companies. The inner `for` loops go over each of those companies and fetch that company specific metrics. Finally, the companies and their respective data is returned to `main.py` file where it is appended to the global `companies` list and converted to [scraped_company_data.csv](data/scraped_company_data.csv) file. This file requires data transformation in the next step.

### Alternative Approach (Scraping Parallelly)
Using traditional approach, scraping financial data for 1500 companies one-by-one might take a significant amount of time (several hours) depending on your network bandwidth. A better and faster approach would be to split the task into multiple scraper instances that will scrape data parallely. Each scraper will be assigned to scrape financial data of the companies belonging to a particular industry.

To do this, you can simply create 8 copies of the `main.py` file (for 8 industries) and modify each `main.py` to fetch companies only for a particular industry. Now, run all the copies parallelly and merge the output CSV files.

Alternatively, you can use Python's `multiprocessing` module to spawn multiple processes to accomplish the same task.

Be sure to rename the final merged CSV file as [scraped_company_data.csv](data/scraped_company_data.csv) (this file requires data transformation in the next step)

## 🔄 Transform and Clean the data
```bash
python data_transformation/transform_data.py
```
At this stage, you will get a file named [transformed_company_data.csv](data/transformed_company_data.csv) (you can load this file into Tableau as Text file)

## ✉️ Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zibran-zarif-amio-b82717263/) [![Mail](https://img.shields.io/badge/Gmail-EA4335?logo=gmail&logoColor=fff)](mailto:zibran.zarif.amio@gmail.com)