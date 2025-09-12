import pandas as pd

def read_csv_in_chunks(file_path, chunk_size=None):
    if chunk_size is not None:
        chunk_iterator = pd.read_csv(file_path, chunksize=chunk_size)
        for chunk in chunk_iterator:
            yield chunk
    else:
        return pd.read_csv(file_path)

# Example usage
file_name = "data.csv"
# To read the whole file
df = read_csv_in_chunks(file_name)
print(df)

# To read in chunks of size 1000
for chunk in read_csv_in_chunks(file_name, chunk_size=1000):
    print(chunk)
