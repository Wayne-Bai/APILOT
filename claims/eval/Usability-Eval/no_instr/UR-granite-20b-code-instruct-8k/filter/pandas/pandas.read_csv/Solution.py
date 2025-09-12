import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('file.csv')

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    print(row)
