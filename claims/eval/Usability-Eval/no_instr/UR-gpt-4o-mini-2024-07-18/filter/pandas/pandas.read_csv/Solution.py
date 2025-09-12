import pandas as pd

# Read the CSV file into a DataFrame
# You can specify the 'chunksize' parameter to iterate over the file in chunks
file_path = 'your_file.csv'  # replace with your file path

# Option 1: Read the entire CSV file into a DataFrame
df = pd.read_csv(file_path)

# Option 2: Read the CSV file in chunks
chunk_size = 1000  # specify your desired chunk size
chunks = pd.read_csv(file_path, chunksize=chunk_size)

# To process each chunk, you can iterate over them
for chunk in chunks:
    # Perform operations on each chunk
    print(chunk.head())  # Example operation: print the first few rows of the chunk
