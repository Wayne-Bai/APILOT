# Import the pandas library
import pandas as pd

# Function to read csv file into DataFrame
def read_csv_file(file_path, chunk_size=None):
    """
    Reads a csv file into a pandas DataFrame.

    Args:
    file_path (str): The path to the csv file.
    chunk_size (int, optional): The number of rows to include in each chunk. Defaults to None.

    Returns:
    pandas.DataFrame or pandas.io.parsers.TextFileReader: A DataFrame if chunk_size is None, otherwise a TextFileReader.
    """
    try:
        # Check if chunk_size is provided
        if chunk_size is None:
            # Read the entire csv file into a DataFrame
            df = pd.read_csv(file_path)
            return df
        else:
            # Read the csv file in chunks
            chunk_reader = pd.read_csv(file_path, chunksize=chunk_size)
            return chunk_reader

    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"File {file_path} is empty.")
        return None
    except pd.errors.ParserError as e:
        print(f"Error parsing file {file_path}: {e}")
        return None

# Example usage:
file_path = 'data.csv'
df = read_csv_file(file_path)
print(df.head())  # Print the first few rows of the DataFrame

# Read the csv file in chunks
chunk_size = 1000
chunk_reader = read_csv_file(file_path, chunk_size)
for chunk in chunk_reader:
    print(chunk.head())  # Print the first few rows of each chunk
