import pandas as pd

# Read HTML tables into a list of DataFrame objects
url = 'https://example.com/table1.html'
html_table = pd.read_html(url)[0]

url = 'https://example.com/table2.html'
html_table = pd.read_html(url)[0]

# Add more URLs and their corresponding HTML tables to the list
