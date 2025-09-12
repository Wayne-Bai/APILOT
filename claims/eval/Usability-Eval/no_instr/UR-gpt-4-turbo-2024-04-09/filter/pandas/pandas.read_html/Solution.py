import pandas as pd

url = 'https://www.example.com'
tables = pd.read_html(url)  # This reads all tables on the page into a list of DataFrame objects
