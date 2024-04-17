# Tableau Industry Insights Dashboard
A comprehensive financial analysis dashboard comparing the financial performance and key metrics of companies across 8 industries (tech, pharmaceutical, real estate, oil & gas, retail, insurance, food, and electricity). Utilizing a [dataset](https://github.com/zzarif/Tableau-Industry-Insights-Dashboard/blob/main/companies/transformed_companies_data.csv) containing financial information for 1500 companies, the dashboard offers a wide range of visualizations and metrics, including market capitalization distribution, year-over-year growth, price-to-earnings ratios, geographical distribution, and more. By comparing and contrasting the performance of companies within each sector, the project uncovers valuable insights for businesses, investors, and other stakeholders.

# Build from Sources
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
4. Scrape and extract the data
```bash
python companies/main.py
```
At this stage, you will get a file named [companies_data.csv](https://github.com/zzarif/Tableau-Industry-Insights-Dashboard/blob/main/companies/companies_data.csv) (this file requires data transformation and cleaning)

5. Transform and clean the data
```bash
python companies/transform_data.py
```
At this stage, you will get a file named [transformed_companies_data.csv](https://github.com/zzarif/Tableau-Industry-Insights-Dashboard/blob/main/companies/transformed_companies_data.csv) (this file can be loaded into Tableau)