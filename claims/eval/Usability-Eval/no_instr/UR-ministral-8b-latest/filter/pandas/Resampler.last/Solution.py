import pandas as pd

def last_non_null_entry(df):
    return df.iloc[::-1].bfill().iloc[0]

# Sample DataFrame
data = {
    'A': [1, 2, 3, None, None],
    'B': [None, None, 3, 4, 5],
    'C': [None, 1, 2, 3, None]
}
df = pd.DataFrame(data)

# Compute the last non-null entry of each column
result = {col: last_non_null_entry(df[[col]]) for col in df.columns}
result_df = pd.DataFrame(result).T

print(result_df)
