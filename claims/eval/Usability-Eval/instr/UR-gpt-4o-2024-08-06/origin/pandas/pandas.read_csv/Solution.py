import pandas as pd

# Define the filename
file_name = 'your_file.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_name)

# If chunking is required, specify the chunk size
chunk_size = 1000  # Define the number of rows per chunk

# Use a TextFileReader to iterate over chunks
chunk_reader = pd.read_csv(file_name, chunksize=chunk_size)

# Iterate over chunks if needed
for chunk in chunk_reader:
    # Process each chunk here
    print(chunk.head())  # Example processing: print the first few rows of each chunk
