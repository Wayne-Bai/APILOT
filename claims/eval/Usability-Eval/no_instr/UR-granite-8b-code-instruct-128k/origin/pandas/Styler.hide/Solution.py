import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
 'A': [1, 2, 3],
 'B': [4, 5, 6],
 'C': [7, 8, 9]
})

# Hide the entire index
df.index = pd.RangeIndex(0, 0)

# Hide the entire column headers
df.columns = pd.RangeIndex(0, 0)

# Print the DataFrame
print(df)
