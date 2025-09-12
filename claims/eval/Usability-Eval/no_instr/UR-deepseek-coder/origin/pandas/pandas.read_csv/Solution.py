import pandas as pd

# Read the entire CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Optionally, iterate over the file in chunks
chunk_size = 10000  # Define the chunk size
for chunk in pd.read_csv('your_file.csv', chunksize=chunk_size):
    # Process each chunk
    print(chunk.head())
