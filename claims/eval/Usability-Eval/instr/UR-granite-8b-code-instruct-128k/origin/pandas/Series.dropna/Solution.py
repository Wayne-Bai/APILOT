import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('data.csv')

# Remove missing values
df.dropna(inplace=True)

# Print the updated DataFrame
print(df)
