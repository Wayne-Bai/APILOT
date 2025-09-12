import pandas as pd
from bs4 import BeautifulSoup

# Function to read HTML tables into a list of DataFrame objects
def read_html_tables(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')

    df_list = []
    for table in tables:
        df = pd.read_html(str(table))[0]  # Read table into a DataFrame
        df_list.append(df)

    return df_list

# Example usage:
# with open('path_to_your_html_file.html', 'r') as file:
#     html_content = file.read()
#     dataframes = read_html_tables(html_content)
#     for i, df in enumerate(dataframes):
#         print(f"DataFrame {i+1}:\n", df)
