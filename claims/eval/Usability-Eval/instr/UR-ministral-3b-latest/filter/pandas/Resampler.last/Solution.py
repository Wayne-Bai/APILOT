import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': [None, 11, None, 14]
})

# Function to get the last non-null entry of each column
def last_non_null(df):
    return df.apply(lambda col: col[col.notna()].iloc[-1], axis=0)

# Apply the function
result = last_non_null(df)
print(result)
