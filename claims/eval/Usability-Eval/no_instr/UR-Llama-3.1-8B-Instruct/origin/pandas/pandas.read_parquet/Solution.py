# Import the necessary library
import pandas as pd

# Load a parquet object from the file path, returning a DataFrame
def load_parquet(file_path):
    try:
        # Use read_parquet() function to load the parquet object
        df = pd.read_parquet(file_path)
        return df
    except Exception as e:
        # Handle any exceptions that may occur during the process
        print(f"An error occurred: {str(e)}")
        return None

# Usage example
file_path = 'path_to_your_file.parquet'  # replace 'path_to_your_file.parquet' with your actual file path
df = load_parquet(file_path)
if df is not None:
    print(df.head())  # Print the first few rows of the DataFrame
