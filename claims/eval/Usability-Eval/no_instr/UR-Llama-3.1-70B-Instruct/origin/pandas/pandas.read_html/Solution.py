# Importing the pandas library
import pandas as pd

# Function to read HTML tables into a list of DataFrame objects
def read_html_tables(url):
    """
    Reads HTML tables from a given URL into a list of DataFrame objects.
    
    Parameters:
    url (str): The URL of the HTML page containing tables.
    
    Returns:
    list: A list of DataFrame objects, each representing a table from the HTML page.
    """
    try:
        # Read HTML tables from the given URL
        tables = pd.read_html(url)
        
        return tables
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
url = "https://www.example.com/tables.html"  # Replace with your URL
tables = read_html_tables(url)

if tables is not None:
    for i, table in enumerate(tables):
        print(f"Table {i+1}:")
        print(table)
        print("\n")
