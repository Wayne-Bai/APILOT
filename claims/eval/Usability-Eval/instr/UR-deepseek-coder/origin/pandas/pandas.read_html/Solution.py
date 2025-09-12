import pandas as pd
from bs4 import BeautifulSoup
import requests

def read_html_tables(url):
    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.content
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all tables in the HTML content
    tables = soup.find_all('table')
    
    # Initialize an empty list to store DataFrame objects
    dfs = []
    
    # Iterate over each table and convert it to a DataFrame
    for table in tables:
        # Convert the table to a DataFrame
        df = pd.read_html(str(table))[0]
        dfs.append(df)
    
    return dfs

# Example usage
url = 'https://example.com/page_with_tables'
tables = read_html_tables(url)

# Print each DataFrame
for i, df in enumerate(tables):
    print(f"Table {i+1}:")
    print(df)
    print("\n")
