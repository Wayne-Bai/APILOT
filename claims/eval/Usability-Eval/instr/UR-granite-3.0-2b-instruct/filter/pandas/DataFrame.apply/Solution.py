import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
   'A': [1, 2, 3],
   'B': [4, 5, 6]
})

# Function to apply
def my_function(x):
   return x * 2

# Apply the function along axis 0 (rows)
df['A'] = df['A'].apply(my_function)

# Apply the function along axis 1 (columns)
df[['A', 'B']] = df[['A', 'B']].apply(my_function)

print(df)
