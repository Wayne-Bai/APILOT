import pandas as pd

# Read a CSV file into a DataFrame
# You can specify `chunksize` to iterate over the file in chunks
df_chunks = pd.read_csv('your_file.csv', chunksize=1000)

# Example of processing each chunk
for chunk in df_chunks:
    # Here you can perform operations on each chunk
    print(chunk)
