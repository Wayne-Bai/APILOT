import pandas as pd

def read_html_tables(url):
    df_list = pd.read_html(url)
    return df_list

# Usage example
# url = 'http://example.com/table.html'
# df_list = read_html_tables(url)
# for i, df in enumerate(df_list, 1):
#     print(f'DataFrame {i}:\n', df, '\n')
