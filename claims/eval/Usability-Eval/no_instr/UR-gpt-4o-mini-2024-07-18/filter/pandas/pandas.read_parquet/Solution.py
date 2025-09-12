import pandas as pd

# Load a parquet object from the file path
file_path = 'your_file_path.parquet'
df = pd.read_parquet(file_path)

# Display the DataFrame
print(df)
