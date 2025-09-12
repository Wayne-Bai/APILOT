
import pandas as pd

# Read csv file
df = pd.read_csv('data.csv')

# Get column names
column_names = df.columns.tolist()

# Print column names
print(column_names)
