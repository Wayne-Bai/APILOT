import pandas as pd

# Reading a CSV file into DataFrame
df = pd.read_csv('your_file.csv')

# To read the CSV file in chunks
chunk_size = 1000  # example chunk size
chunk_iterator = pd.read_csv('your_file.csv', chunksize=chunk_size)

# Example: processing each chunk
for chunk in chunk_iterator:
    # perform operations on each chunk
    print(chunk.head())  # just an example operation
