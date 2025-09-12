import pandas as pd

def read_csv_file(file_path, chunk_size=None):
    """
    Reads a CSV file into a pandas DataFrame. Defaults to reading the entire
    file into a single DataFrame. If chunk_size is specified, reads the
    file into chunks.

    Parameters:
    - file_path: The path to the CSV file to be read.
    - chunk_size: The number of rows to read at a time. If set, the function
                  will return an iterator.

    Returns:
    - data_frames: An iterator yielding one chunk at a time for the
                   'chunk_size' case, or a single DataFrame for the
                   'chunk_size' not set case.
    """
    if chunk_size is not None:
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            yield chunk
    else:
        return pd.read_csv(file_path)

# Example usage:
file_path = 'path_to_your_csv_file.csv'
# To read entire file
all_data_df = read_csv_file(file_path)
print(all_data_df.head())

# To read in chunks
chunk_size = 1000
for chunk in read_csv_file(file_path, chunk_size=chunk_size):
    print(chunk.head())
