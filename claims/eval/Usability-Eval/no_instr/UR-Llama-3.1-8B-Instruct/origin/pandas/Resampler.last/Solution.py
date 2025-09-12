import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': [6, None, 8, 9, 10],
    'C': [11, 12, None, 14, 15]
})

# Compute the last non-null entry of each column
last_non_null = df.notnull().cumsum().eq(1).idxmax()

# Print the result
print("Last non-null entry of each column:")
print(last_non_null)
print("\nCorresponding values:")
print(df.loc[last_non_null])
