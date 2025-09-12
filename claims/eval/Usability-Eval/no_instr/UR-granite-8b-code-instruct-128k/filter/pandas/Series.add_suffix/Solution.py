import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Add a suffix to column labels
df.columns = df.columns.str.cat(suffix='_new')

# Print the updated DataFrame
print(df)
