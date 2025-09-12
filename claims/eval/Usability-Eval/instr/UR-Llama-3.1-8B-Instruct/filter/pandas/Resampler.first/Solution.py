# Import pandas library
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, None, 3, 4, None],
    'B': [None, 2, None, 5, 6],
    'C': [7, None, None, None, 9]
})

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Compute the first non-null entry of each column
first_non_null = df.apply(lambda x: x[x.notnull()].iloc[0], axis=0)

# Print the result
print("\nFirst non-null entry of each column:")
print(first_non_null)
