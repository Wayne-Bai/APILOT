import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
}

df = pd.DataFrame(data)

# Remove missing values
df_cleaned = df.dropna(how='any')

print(df_cleaned)
