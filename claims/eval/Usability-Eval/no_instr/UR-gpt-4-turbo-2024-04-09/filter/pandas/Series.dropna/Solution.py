import pandas as pd

# Sample DataFrame with missing values
data = {
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': [9, 10, 11, None]
}
df = pd.DataFrame(data)

# Removing rows with any missing values
df_cleaned = df.dropna()

print(df_cleaned)
