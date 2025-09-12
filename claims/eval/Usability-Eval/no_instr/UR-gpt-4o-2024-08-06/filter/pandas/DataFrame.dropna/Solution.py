import pandas as pd

# Sample DataFrame with missing values
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None],
    'C': [7, None, 9, 10]
}
df = pd.DataFrame(data)

# Remove rows with any missing values
df_cleaned = df.dropna()

print(df_cleaned)
