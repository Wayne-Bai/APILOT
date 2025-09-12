import pandas as pd

# Create a simple dataframe
df = pd.DataFrame({
   'A': [1, 2, 3],
   'B': [4, 5, 6]
})

# Define a function to apply elementwise
def apply_function(row):
   return row['A'] + row['B']

# Apply the function to the dataframe
df['C'] = df.apply(apply_function, axis=1)
