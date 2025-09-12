# Import pandas library and assign it a shorter alias 'pd'
import pandas as pd

# Function to read a comma-separated values (csv) file into DataFrame
def read_csv_file(file_path, chunksize=10 ** 6):
    """
    Read a comma-separated values (csv) file into DataFrame.

    Parameters:
    ----------
    file_path : str
        The path to the csv file.
    chunksize : int, optional
        The number of rows in each chunk. The default is 10^6.

    Yields:
    -------
    pd.DataFrame
        A DataFrame with a subset of the rows from the csv file.
    """
    try:
        # Use pandas.read_csv() to read the csv file into DataFrame
        df = pd.read_csv(file_path, chunksize=chunksize)
        
        # Iterate over the chunks and yield each chunk
        for chunk in df:
            yield chunk
    except pd.errors.EmptyDataError:
        print(f"No data in file {file_path}")
    except pd.errors.ParserError as e:
        print(f"Error parsing file {file_path}: {e}")

# Example usage:
if __name__ == "__main__":
    file_path = "path_to_your_csv_file.csv"  # Replace 'path_to_your_csv_file.csv' with the path to your csv file
    for i, chunk in enumerate(read_csv_file(file_path)):
        print(f"Chunk {i+1}:")
        print(chunk)
        print("\n")
