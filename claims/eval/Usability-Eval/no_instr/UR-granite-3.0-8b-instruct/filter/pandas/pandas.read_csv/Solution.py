import pandas as pd

# Read the entire CSV file into a DataFrame
df = pd.read_csv('file.csv')

# Read the CSV file into a DataFrame, iterating over the file in chunks
chunksize = 10000
for chunk in pd.read_csv('file.csv', chunksize=chunksize):
    # Process each chunk here
    print(chunk)
