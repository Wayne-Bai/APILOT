import pandas as pd

# URL pointing to a webpage containing HTML tables
url = 'http://example.com/somepage_with_tables.html'

# Use pandas to read HTML tables from the webpage
tables = pd.read_html(url)

# Check the number of tables and print each table
print(f"Number of tables found: {len(tables)}")
for index, table in enumerate(tables):
    print(f"\nTable {index}:")
    print(table)
