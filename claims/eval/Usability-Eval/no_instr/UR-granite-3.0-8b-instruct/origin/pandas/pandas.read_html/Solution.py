import pandas as pd

# Assuming the HTML files are in the same directory as your Python script
html_files = ['file1.html', 'file2.html', 'file3.html']

dfs = []
for file in html_files:
    df = pd.read_html(file)[0]  # Assuming the first table in the HTML file is the one you want to read
    dfs.append(df)
