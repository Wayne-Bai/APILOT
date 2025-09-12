
import pandas as pd

# Define the input mapping or function
mapping = {'A': 1, 'B': 2, 'C': 3}

# Create a sample DataFrame
df = pd.DataFrame({'col': ['A', 'B', 'C', 'A', 'B']})

# Map the values in the 'col' column using the input mapping
df['col'] = df['col'].map(mapping)

# Output the updated DataFrame
print(df)

