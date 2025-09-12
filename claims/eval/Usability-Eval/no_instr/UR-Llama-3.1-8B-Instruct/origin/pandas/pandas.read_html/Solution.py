import pandas as pd

def read_html_tables(url):
    try:
        # Read HTML tables into a list of DataFrame objects
        tables = pd.read_html(url)
        
        # Print the list of DataFrames
        for i, df in enumerate(tables):
            print(f"Table {i+1}:")
            print(df.head())  # Print the first few rows of each table
            print("\n")
        
        # Return the list of DataFrames
        return tables
    
    except Exception as e:
        print(f"Error reading HTML tables: {e}")

# Example usage:
url = "https://en.wikipedia.org/wiki/List_of_mountains_of_Switzerland"
tables_list = read_html_tables(url)
