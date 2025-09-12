import pandas as pd

def load_parquet_to_df(file_path):
    """
    Load a parquet object from the file path, returning a DataFrame.
    
    Parameters:
    file_path (str): The path to the parquet file.
    
    Returns:
    pd.DataFrame: A DataFrame containing the data from the parquet file.
    """
    try:
        # Load the parquet object from the file path
        df = pd.read_parquet(file_path, engine='pyarrow')
        
        return df
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = 'path_to_your_parquet_file.parquet'  # replace with your file path
df = load_parquet_to_df(file_path)
print(df.head())
