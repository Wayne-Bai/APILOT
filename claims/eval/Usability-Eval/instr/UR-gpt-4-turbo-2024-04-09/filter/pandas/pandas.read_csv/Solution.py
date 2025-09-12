import pandas as pd

def read_csv_in_chunks(file_path, chunk_size=None):
    if chunk_size:
        return pd.read_csv(file_path, chunksize=chunk_size)
    else:
        return pd.read_csv(file_path)

# Example usage:
# df = read_csv_in_chunks('your_file.csv')
# For reading in chunks: df_chunks = read_csv_in_chunks('your_file.csv', chunk_size=1000)
