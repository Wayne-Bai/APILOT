import pandas as pd

def read_csv_file(file_path, chunksize=None):
    chunks = []
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        chunks.append(chunk)
    return pd.concat(chunks)

# Usage
df = read_csv_file('file.csv', chunksize=5000)
