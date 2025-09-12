import pandas as pd

# Read HTML tables into a list of DataFrame objects
def read_html_tables(url):
    """
    Reads HTML tables from a given URL into a list of DataFrame objects.
    
    Args:
        url (str): URL of the HTML page containing tables.
    
    Returns:
        list: A list of pandas DataFrame objects, each representing an HTML table.
    """
    try:
        dfs = pd.read_html(url)
        return dfs
    except Exception as e:
        print(f"Error reading HTML tables: {e}")
        return []

# Example usage:
url = "https://www.w3schools.com/html/html_tables.asp"  # Replace with your URL
dfs = read_html_tables(url)

# Print the first DataFrame (first table) if it exists
if dfs:
    print(dfs[0].head())
else:
    print("No tables found.")
