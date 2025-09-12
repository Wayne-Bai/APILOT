import pandas as pd

# Load a parquet object from the file path and return as a DataFrame
file_path = 'your_file_path_here.parquet'
df = pd.read_parquet(file_path)

# Display the DataFrame
print(df)
