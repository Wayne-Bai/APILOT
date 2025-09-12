import pandas as pd

# Load a parquet object from the file path, returning a DataFrame
file_path = 'your_file_path.parquet'  # Replace with your actual file path
df = pd.read_parquet(file_path)

# Display the resulting DataFrame
print(df)
