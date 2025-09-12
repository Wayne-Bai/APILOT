import pandas as pd

# URL of the webpage
url = "https://your-website.com"

# Use pandas to read all tables on the webpage and return a list of DataFrame
tables = pd.read_html(url)

# Print the first table
print(tables[0])
