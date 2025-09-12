import pandas as pd

# Assuming we have a pandas DataFrame df
df = pd.DataFrame({
    'Name': ['John', 'Ann', 'Peter'],
    'Age': [28, 24, 33]
})

# Convert DataFrame to dictionary
dict_from_df = df.to_dict('list')
print(dict_from_df)
