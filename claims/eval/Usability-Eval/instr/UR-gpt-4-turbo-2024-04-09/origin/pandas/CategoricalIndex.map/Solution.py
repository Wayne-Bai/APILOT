import pandas as pd

# Assuming you have a DataFrame and you want to map values in a specific column
data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Values': [100, 200, 300, 400, 500, 600]
}
df = pd.DataFrame(data)

# Define the mapping (could be a dictionary or a function)
mapping = {'A': 'Alpha', 'B': 'Beta', 'C': 'Gamma'}

# Use the map method to remap values in the Category column
df['Category'] = df['Category'].replace(mapping)

print(df)
