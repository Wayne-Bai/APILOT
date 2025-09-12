import pandas as pd

# Read the CSV file
df = pd.read_csv('your_file.csv')

# Infer better dtypes for object columns
df = df.convert_dtypes()
