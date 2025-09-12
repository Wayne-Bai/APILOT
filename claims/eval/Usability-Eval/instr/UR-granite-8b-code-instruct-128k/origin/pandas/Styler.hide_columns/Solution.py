import pandas as pd

# Read in the CSV file
df = pd.read_csv('file.csv')

# Hide the column headers
df.columns = [''] * len(df.columns)

# Print the resulting DataFrame
print(df)
