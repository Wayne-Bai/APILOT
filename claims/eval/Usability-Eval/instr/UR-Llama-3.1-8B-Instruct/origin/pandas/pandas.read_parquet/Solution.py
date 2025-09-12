# Import the pandas library, which we will use to read the parquet file
import pandas as pd

# Specify the path to the parquet file
# Replace 'path_to_your_file.parquet' with the actual path to your parquet file
path_to_parquet_file = 'path_to_your_file.parquet'

# Use the pd.read_parquet function to load the parquet file into a DataFrame
def load_parquet_file(path):
    try:
        df = pd.read_parquet(path)
        return df
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Load the parquet file into a DataFrame
df = load_parquet_file(path_to_parquet_file)

# Print the first few rows of the DataFrame to verify that the data was loaded correctly
print(df.head())
