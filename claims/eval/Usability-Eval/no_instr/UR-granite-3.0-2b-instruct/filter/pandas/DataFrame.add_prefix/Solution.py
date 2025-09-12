import pandas as pd

# Sample Series
s = pd.Series([1, 2, 3, 4, 5])
s.name = 'Original'

# Prefix labels for Series
s.name = 'Prefixed'

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
df.name = 'Original'

# Prefix labels for DataFrame
df.columns = ['Prefixed']

print(s)
print(df)
