# Import necessary libraries
import pandas as pd

# Function to read csv file into DataFrame
def read_csv_file(file_path, chunksize=None):
    """
    Reads a comma-separated values (csv) file into DataFrame.
    
    Args:
        file_path (str): Path to the csv file.
        chunksize (int, optional): Number of rows in each chunk. Defaults to None.
        
    Returns:
        pd.DataFrame: DataFrame containing the data from the csv file.
    """
    
    # Read csv file into DataFrame with optional chunking
    try:
        # If chunksize is not provided, read entire file
        if chunksize is None:
            df = pd.read_csv(file_path)
        # If chunksize is provided, read file in chunks
        else:
            chunk = pd.read_csv(file_path, chunksize=chunksize)
            df = pd.concat(chunk, ignore_index=True)
        return df
    except FileNotFoundError:
        print("File not found at the specified path.")
        return None
    except pd.errors.EmptyDataError:
        print("File is empty.")
        return None
    except pd.errors.ParserError:
        print("Error parsing the file.")
        return None

# Example usage:
if __name__ == "__main__":
    file_path = 'data.csv'  # replace with your csv file path
    chunksize = 10  # number of rows in each chunk
    
    df = read_csv_file(file_path, chunksize)
    
    if df is not None:
        print(df.head())  # print the first few rows of the DataFrame
