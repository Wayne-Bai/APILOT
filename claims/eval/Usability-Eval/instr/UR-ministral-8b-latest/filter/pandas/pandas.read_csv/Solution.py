import pandas as pd

def read_csv(file_path, chunk_size=None):
    if chunk_size is not None:
        chunks = []
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            chunks.append(chunk)
        return pd.concat(chunks, axis=0)
    else:
        return pd.read_csv(file_path)

# Usage example:
# df = read_csv('your_file.csv')
# df = read_csv('your_file.csv', chunk_size=10000)  # Read file in chunks of 10,000 rows
