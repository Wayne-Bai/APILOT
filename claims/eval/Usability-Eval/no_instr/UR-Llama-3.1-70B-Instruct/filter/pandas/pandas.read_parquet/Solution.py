# Importing pandas library
import pandas as pd

# Function to load parquet object from file path
def load_parquet_file(file_path):
    """
    Load a parquet object from the file path, returning a DataFrame.
    
    Args:
        file_path (str): The path to the parquet file.
    
    Returns:
        pd.DataFrame: A DataFrame loaded from the parquet file.
    """
    try:
        # Load the parquet file into a DataFrame
        df = pd.read_parquet(file_path)
        
        return df
    
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage:
file_path = 'path_to_your_parquet_file.parquet'  # Replace with your parquet file path
df = load_parquet_file(file_path)

# Print the first few rows of the DataFrame
if df is not None:
    print(df.head())
