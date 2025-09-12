import pandas as pd

def read_csv_with_chunks(file_path, chunk_size=None):
    if chunk_size:
        return pd.read_csv(file_path, chunksize=chunk_size)
    else:
        return pd.read_csv(file_path)

# Example usage:
file_path = 'your_file.csv'

# Read the entire file
df = read_csv_with_chunks(file_path)
print(df.head())

# Or, read the file in chunks
chunks = read_csv_with_chunks(file_path, chunk_size=10000)
for chunk in chunks:
    print(chunk.head())
    # Process each chunk as needed
