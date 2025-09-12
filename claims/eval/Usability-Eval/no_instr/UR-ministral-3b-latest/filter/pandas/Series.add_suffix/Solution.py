import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2],
    'B': [3, 4]
}
df = pd.DataFrame(data)

# Function to suffix column labels
def suffix_columns(df, suffix):
    return df.add_suffix('_suffix')

# Add Suffix 'suffix' to column labels
df = suffix_columns(df, 'suffix')

print(df)
