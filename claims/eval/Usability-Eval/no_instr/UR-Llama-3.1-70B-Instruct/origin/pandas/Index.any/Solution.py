import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 0, 1, 1],
    'B': [0, 1, 1, 1],
    'C': [1, 1, 1, 0]
})

# Use the any() function to check for any truthy element in each column
print(df.any())

# Output:
# A    True
# B    True
# C    True
# dtype: bool

# Use the any() function on the entire DataFrame
print(df.values.any())

# Output: True

# Use the any() function with axis=1 to check for any truthy element in each row
print(df.any(axis=1))

# Output:
# 0    True
# 1    True
# 2    True
# 3    True
# dtype: bool
