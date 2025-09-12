import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Define a function to be applied along the rows
def add_10(row):
    return row + 10

# Apply the function along the rows
df_with_10 = df.apply(add_10, axis=1)

# Print the resulting DataFrame
print(df_with_10)
