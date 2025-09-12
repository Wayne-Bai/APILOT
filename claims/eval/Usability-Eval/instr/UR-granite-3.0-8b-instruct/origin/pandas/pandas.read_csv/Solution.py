import pandas as pd

# Read a CSV file into a DataFrame
df = pd.read_csv('file.csv')

# To iterate or break the file into chunks
chunksize = 10000
for chunk in pd.read_csv('file.csv', chunksize=chunksize):
    # Process each chunk here
    print(chunk.head())
