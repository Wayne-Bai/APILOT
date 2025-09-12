import pandas as pd

# Sample DataFrame
data = {'Category': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)

# Define mapping
value_mapping = {'A': 'Alpha', 'B': 'Beta', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo'}

# Map values using the mapping
df['Mapped_Category'] = df['Category'].map(value_mapping)

print(df)
