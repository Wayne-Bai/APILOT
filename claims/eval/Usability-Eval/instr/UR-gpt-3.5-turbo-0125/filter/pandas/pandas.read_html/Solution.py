
import pandas as pd

url = 'url_to_html_page'
dfs = pd.read_html(url)

for i, df in enumerate(dfs):
    print(f"DataFrame {i+1}:")
    print(df)
