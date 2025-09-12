import pandas as pd

# Read HTML tables into a list of DataFrame objects
url = 'your_url_here'  # Replace with the actual URL containing the HTML tables
dfs = pd.read_html(url)

# dfs now contains a list of DataFrame objects, one for each table found in the HTML
