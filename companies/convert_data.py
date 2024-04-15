from columns import columns
from selenium.webdriver.common.by import By


# convert html table row to dictionary
def get_dict_from_html_row(row, industry):
    contents = {}
    contents[columns[0]] = row.find_element(By.CLASS_NAME, "company-name").text # company
    contents[columns[1]] = row.find_element(By.TAG_NAME, "a").get_attribute("href").rsplit('/', 2)[0] # company path
    contents[columns[2]] = industry # industry (static value)
    contents[columns[3]] = row.find_element(By.CLASS_NAME, "responsive-hidden").text # country
    contents[columns[4]] = row.find_elements(By.CLASS_NAME, "td-right")[1].get_attribute("data-sort") # employees
    return contents


# convert string to numbers (decimal)
def get_number_from_string(value):
    value = value.replace("$", "").strip() # remove $ if present
    if value.endswith("Trillion") or value.endswith("T"):
        return float(value.split(" ")[0]) * 1e12
    elif value.endswith("Billion") or value.endswith("B"):
        return float(value.split(" ")[0]) * 1e9
    elif value.endswith("Million") or value.endswith("M"):
        return float(value.split(" ")[0]) * 1e6
    elif value.endswith("%"):
        return float(value[:-1]) / 100
    else:
        return float(value)