import pandas as pd

# Sample DataFrame with missing values
data = {
    'A': [1, 2, None, 4],
    'B': [None, 'b', 'c', 'd'],
    'C': [1.1, None, 3.3, 4.4]
}

df = pd.DataFrame(data)

# Remove missing values
df_cleaned = df.dropna()

print(df_cleaned)
