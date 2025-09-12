import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': [None, 'dog', 'cat', 'mouse'],
    'C': [10, None, 30, 40]
}

df = pd.DataFrame(data)

# Remove missing values
df_cleaned = df.dropna()

print(df_cleaned)
