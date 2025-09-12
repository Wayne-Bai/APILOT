import pandas as pd

def map_values(df, mapping_dict):
    return df.replace(mapping_dict)

# Example usage:
data = {'col1': ['a', 'b', 'c'], 'col2': [1, 2, 3]}
df = pd.DataFrame(data)
mapping_dict = {'a': 'x', 'b': 'y'}
df = map_values(df, mapping_dict)
print(df)
