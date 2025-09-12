
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# Define a custom function to apply along the axis
def custom_function(row):
    return row['A'] + row['B'] * row['C']

# Apply the function along the rows (axis=1)
df['result'] = df.apply(custom_function, axis=1)

print(df)
