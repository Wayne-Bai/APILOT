import pandas as pd

# Suppose we have a DataFrame df
df = pd.DataFrame({
   'A': [1, 2, 3, 4, 5],
   'B': [10, 20, 30, 40, 50]
})

# Suppose we want to map values in column 'A' with a function that squares the input
mapping_function = lambda x: x**2

# We can use the map method on a Series to apply the function to each value
df['A'] = df['A'].map(mapping_function)

print(df)
