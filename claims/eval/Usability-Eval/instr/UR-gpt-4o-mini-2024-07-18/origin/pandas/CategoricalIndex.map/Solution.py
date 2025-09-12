import pandas as pd

# Sample DataFrame
data = {'Category': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)

# Define a mapping dictionary
mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

# Map values in the 'Category' column using the mapping dictionary
df['Mapped'] = df['Category'].replace(mapping)

print(df)
