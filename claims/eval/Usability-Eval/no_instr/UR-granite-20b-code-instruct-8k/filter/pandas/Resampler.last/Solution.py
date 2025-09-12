import pandas as pd

# Assuming the data is in a CSV file named 'data.csv'
df = pd.read_csv('data.csv')

# Compute the last non-null entry of each column
last_non_null = df.iloc[-1]

# Print the results
print(last_non_null)
