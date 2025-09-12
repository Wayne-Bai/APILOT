import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': [None, None, 3, None],
    'C': [7, 8, 9, None]
}

df = pd.DataFrame(data)

# Function to find last non-null entry of each column
def last_non_null(df):
    return df.apply(lambda col: col.dropna().iloc[-1])

# Compute the last non-null entry of each column
last_non_null_values = last_non_null(df)
print(last_non_null_values)
