
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Define a function to apply along the rows
def row_func(row):
    return row['A'] + row['B'] + row['C']

# Apply the function along the rows
df['Sum'] = df.apply(row_func, axis=1)

# Print the resulting DataFrame
print(df)
