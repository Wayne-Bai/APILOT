import pandas as pd
url = "your_url_here" # replace with the actual URL of the HTML table
tables = pd.read_html(url) 