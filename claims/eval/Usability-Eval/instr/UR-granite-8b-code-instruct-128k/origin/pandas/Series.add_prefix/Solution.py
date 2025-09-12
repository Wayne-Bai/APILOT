
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Define the prefix string
prefix_string = 'Prefix_'

# Add the prefix to the column names
df.columns = [prefix_string + column for column in df.columns]

# Print the updated DataFrame
print(df)
