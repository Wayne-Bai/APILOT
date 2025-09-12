import pandas as pd

# URL of the webpage containing the HTML tables
url = "http://example.com"

# Reading all tables into a list of DataFrame objects
tables = pd.read_html(url)

# Printing the first table for verification
print(tables[0])
