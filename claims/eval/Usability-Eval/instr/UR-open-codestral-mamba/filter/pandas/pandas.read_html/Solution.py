import pandas as pd

url = "http://example.com"  # replace with your URL
tables = pd.read_html(url)

# print the list of dataframes
for df in tables:
    print(df)
