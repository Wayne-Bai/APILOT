import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
   'A': [1, 2, 3],
   'B': [4, 5, 6]
})

# Define a function to apply
def multiply_by_two(x):
    return x * 2

# Apply the function along axis 0 (rows)
df['A'] = df['A'].apply(multiply_by_two)

# Apply the function along axis 1 (columns)
df[['A', 'B']] = df[['A', 'B']].apply(lambda x: x * 2)

print(df)
