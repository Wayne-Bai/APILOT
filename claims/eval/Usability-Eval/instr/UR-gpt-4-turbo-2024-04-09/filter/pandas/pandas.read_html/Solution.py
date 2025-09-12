import pandas as pd

# Assuming 'example.html' contains the HTML tables you want to read
url = 'example.html'
tables = pd.read_html(url)  # This will return a list of DataFrame objects from the tables in the HTML file
