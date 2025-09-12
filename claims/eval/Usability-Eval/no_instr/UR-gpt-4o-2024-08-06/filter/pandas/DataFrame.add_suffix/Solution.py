import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Suffix for column labels
suffix = '_suffix'

# Applying the suffix to each column label
df = df.add_suffix(suffix)

print(df)
