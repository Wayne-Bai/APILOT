import pandas as pd

# Load Parquet file into a DataFrame
file_path = "path_to_your_parquet_file.parquet"  # replace with your file path
dataframe = pd.read_parquet(file_path)

print(dataframe.head())  # view the first 5 rows of the dataframe
