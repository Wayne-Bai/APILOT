import pandas as pd

# Let's assume we have the following DataFrame
df = pd.DataFrame({
   'A': ['foo', 'bar', 'baz'],
   'B': ['one', 'one', 'two'],
   'C': ['x', 'y', 'z'],
   'D': [1, 2, 3]
})

# To suffix labels, we'll utilize the add_suffix method
suffix = '_suffixed'
df = df.add_suffix(suffix)

print(df)  # This will print the DataFrame with suffixed labels
