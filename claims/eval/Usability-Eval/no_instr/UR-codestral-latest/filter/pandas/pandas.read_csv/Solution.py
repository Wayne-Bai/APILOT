import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Optionally, read the CSV file in chunks
chunk_size = 500 # define the size of chunks
chunks = []
for chunk in pd.read_csv('your_file.csv', chunksize=chunk_size):
    chunks.append(chunk)

# Concatenate all chunks into a single DataFrame
df = pd.concat(chunks, axis=0)
