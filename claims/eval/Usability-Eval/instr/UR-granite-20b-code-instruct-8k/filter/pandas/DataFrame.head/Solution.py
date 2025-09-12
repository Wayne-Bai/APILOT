import pandas as pd

# Read data from a CSV file
data = pd.read_csv('filename.csv')

# Return the first n rows
first_n_rows = data.head(n)

# Print the first n rows
print(first_n_rows)
