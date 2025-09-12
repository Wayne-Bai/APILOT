import pandas as pd

# Assuming we have a dataframe called df
df = pd.DataFrame({
   'A': [1, 2, 3],
   'B': [4, 5, 6]
})

# Get the dictionary representation of the dataframe
dict_from_df = df.to_dict()

print(dict_from_df)
