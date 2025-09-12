import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Suffix to add to column labels
suffix = '_new'

# Adding suffix to column labels
df = df.add_suffix(suffix)

print(df)
