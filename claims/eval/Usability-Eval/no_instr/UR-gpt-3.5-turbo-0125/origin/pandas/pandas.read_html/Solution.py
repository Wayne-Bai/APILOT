
import pandas as pd

url = 'https://www.w3schools.com/html/html_tables.asp'
tables_list = pd.read_html(url)

for idx, table in enumerate(tables_list):
    print(f"Table {idx + 1}:")
    print(table)
