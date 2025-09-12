import pandas as pd

def map_values(df, mapping_dict):
    return df.replace(mapping_dict)

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': ['a', 'b', 'a', 'b', 'a']
})

mapping_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

new_df = map_values(df, mapping_dict)
print(new_df)
