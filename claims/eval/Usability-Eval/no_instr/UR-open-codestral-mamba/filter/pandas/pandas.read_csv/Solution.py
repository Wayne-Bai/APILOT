import pandas as pd

# Read a CSV file into a DataFrame
df = pd.read_csv('filename.csv')

# Optionally, read the file in chunks
chunksize = 5 * 10 ** 5  # adjust this value based on your system's memory capacity
chunks = []
chunks = pd.read_csv('filename.csv', chunksize=chunksize)
for chunk in chunks:
    process(chunk)  # apply your processing here
