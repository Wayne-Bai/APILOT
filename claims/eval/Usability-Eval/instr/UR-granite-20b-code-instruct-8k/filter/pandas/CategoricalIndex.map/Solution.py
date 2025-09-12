import pandas as pd
# Create a sample DataFrame
df = pd.DataFrame({'column1': ['a', 'b', 'c'], 'column2': [1, 2, 3]})
# Define a mapping dictionary
mapping = {'a': 10, 'b': 20, 'c': 30}
# Use the map() function to map values in the 'column1' column
df['column1'] = df['column1'].map(mapping)
# Print the updated DataFrame
print(df)
