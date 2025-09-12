import pandas as pd

# Let's assume we have a DataFrame `df` and the string prefix we want to add is "Prefix_"

# Adding the prefix to every label in the DataFrame
df = df.add_prefix('Prefix_')

# Print the updated DataFrame
print(df)
