 
# Importing necessary libraries
import pandas as pd
from bs4 import BeautifulSoup
import webbrowser

# Function to read HTML tables into a list of DataFrame objects
def read_html_tables(html_string):
    """
    Read HTML tables into a list of DataFrame objects.
    
    Parameters:
    html_string (str): A string containing the HTML content.
    
    Returns:
    list: A list of DataFrame objects.
    """
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_string, 'html.parser')
    
    # Find all tables in the HTML content
    tables = soup.find_all('table')
    
    # List to store the DataFrame objects
    df_list = []
    
    # Loop through each table and convert it to a DataFrame
    for table in tables:
        df = pd.read_html([table.prettify()][0])[0]
        df_list.append(df)
    
    return df_list

# Usage example:
# Open a URL in the default browser
webbrowser.open('https://example.com')

# Open a local HTML file
html_file = 'example.html'
with open(html_file, 'r') as file:
    html_string = file.read()

# Read HTML tables into a list of DataFrame objects
df_list = read_html_tables(html_string)

# Print the list of DataFrame objects
for i, df in enumerate(df_list):
    print(f"Table {i+1}:")
    print(df)
    print()
