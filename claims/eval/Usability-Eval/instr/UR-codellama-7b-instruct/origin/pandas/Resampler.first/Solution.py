import pandas as pd

# Read in data from a CSV file
df = pd.read_csv("data.csv")

# Convert missing values (NaN) to None
df.fillna(None, inplace=True)

# Compute first non-null entry of each column
first_non_null = df.apply(lambda x: x[x.first_valid_index()], axis=0)
