import pandas as pd
from urls import metric_endpoints

def transform_value(value):
    if pd.isnull(value) or value == "":
        return None
    if isinstance(value, str):
        value = value.replace("$", "").replace(",", "").strip()
        if value.startswith(">") or value.startswith("<"):
            return None
        elif value.endswith("Trillion") or value.endswith("T"):
            return float(value.split(" ")[0]) * 1e12
        elif value.endswith("Billion") or value.endswith("B"):
            return float(value.split(" ")[0]) * 1e9
        elif value.endswith("Million") or value.endswith("M"):
            return float(value.split(" ")[0]) * 1e6
        elif value.endswith("%"):
            return float(value[:-1]) / 100
    try:
        return float(value)
    except ValueError:
        return None

# Read the CSV file
df = pd.read_csv("company_data/companies_data.csv")

# Apply the transformation to the specified columns
for metric in metric_endpoints:
    df[metric] = df[metric].apply(transform_value)

# Save the transformed DataFrame back to a CSV file
df.to_csv("company_data/transformed_companies_data.csv", index=False)