# Import the required library
import pandas as pd

# File path
file_path = 'your_file_path_here.parquet'

# Load the parquet file into a DataFrame
df = pd.read_parquet(file_path)

# Print the DataFrame to verify
print(df.head())
