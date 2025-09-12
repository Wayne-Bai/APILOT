import pandas as pd

# Function to read HTML tables from a given URL
def read_html_tables(url):
    # Use pandas to read HTML tables
    tables = pd.read_html(url)
    return tables

# Example usage
url = 'https://example.com'  # Replace with the actual URL containing HTML tables
dataframes = read_html_tables(url)

# Display the number of tables extracted
print(f"Number of tables extracted: {len(dataframes)}")

# Optionally print the first dataframe as an example
if dataframes:
    print(dataframes[0])
