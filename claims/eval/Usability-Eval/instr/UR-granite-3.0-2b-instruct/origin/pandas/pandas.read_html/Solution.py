import pandas as pd
from bs4 import BeautifulSoup
import requests

# URL of the HTML document
url = 'https://example.com'

# Send HTTP request and get the response
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the tables in the HTML document
tables = soup.find_all('table')

# Initialize an empty list to store the DataFrame objects
dfs = []

# Iterate over the tables and read them into a DataFrame
for table in tables:
    # Remove any HTML tags from the table
    table_text = table.get_text()

    # Parse the table text as a DataFrame
    df = pd.read_csv(pd.compat.StringIO(table_text), sep='\s+')

    # Append the DataFrame to the list
    dfs.append(df)

# Print the list of DataFrame objects
for i, df in enumerate(dfs):
    print(f'DataFrame {i+1}:')
    print(df.head())
    print()
