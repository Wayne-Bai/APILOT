import pandas as pd

# Specify the URL of the HTML page containing tables
url = 'https://example.com/page-with-tables'

# Use read_html to extract tables into a list of DataFrame objects
tables = pd.read_html(url)

# Display the number of tables and their first few records
for index, table in enumerate(tables):
    print(f"Table {index + 1}:\n", table.head())
