import pandas as pd

html_tables = ['<table><tr><th>A</th><th>B</th><th>C</th></tr><tr><td>1</td><td>2</td><td>3</td></tr></table>',
'<table><tr><th>X</th><th>Y</th><th>Z</th></tr><tr><td>4</td><td>5</td><td>6</td></tr></table>']

# Read HTML tables into a list of DataFrames
dfs = []
for html in html_tables:
    df = pd.read_html(html)[0]
    dfs.append(df)
