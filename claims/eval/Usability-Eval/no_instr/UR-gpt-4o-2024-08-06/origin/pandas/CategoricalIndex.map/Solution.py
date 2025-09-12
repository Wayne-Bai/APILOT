import pandas as pd

# Sample DataFrame
data = {'Category': ['A', 'B', 'C', 'D', 'A']}
df = pd.DataFrame(data)

# Mapping dictionary
mapping_dict = {'A': 'Alpha', 'B': 'Beta', 'C': 'Gamma', 'D': 'Delta'}

# Map values using the mapping dictionary
df['Category_Mapped'] = df['Category'].map(mapping_dict)

print(df)
