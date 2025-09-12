
import pandas as pd

# Use the `pd.read_html()` function to read all tables from an HTML file
with open("example.html") as f:
    dfs = pd.read_html(f)

# Print the list of DataFrame objects
print(dfs)
