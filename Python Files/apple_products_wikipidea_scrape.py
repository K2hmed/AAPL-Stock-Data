import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://en.wikipedia.org/wiki/List_of_Apple_products"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all tables with the 'wikitable' class
tables = soup.find_all('table', {'class': 'wikitable'})


combined_data = []

# function to convert date strings to 'YYYY-MM-DD' format
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%B %d, %Y').strftime('%Y-%m-%d')
    except (ValueError, TypeError):
        return None  # Return None for invalid or missing dates


for table in tables[:-1]: # exclude the last table as it's unrelated
    df = pd.read_html(str(table))[0]
    df.columns = df.columns.str.strip()

    # preprocess the 'Released' and 'Discontinued' columns
    if 'Released' in df.columns:
        df['Released'] = df['Released'].apply(parse_date)
    if 'Discontinued' in df.columns:
        df['Discontinued'] = df['Discontinued'].apply(parse_date)

    # append the processed DataFrame to the combined list
    combined_data.append(df)

# combine all tables into a single DataFrame
combined_table = pd.concat(combined_data, ignore_index=True)
combined_table.to_csv('apple_products_release_dates.csv', index=False)
