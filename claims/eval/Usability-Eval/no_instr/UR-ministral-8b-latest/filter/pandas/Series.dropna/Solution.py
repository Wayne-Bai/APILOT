import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, None, 5],
    'C': [1, None, None, 4, None]
}
df = pd.DataFrame(data)

# Remove rows with any missing values
df_clean = df.dropna()

print("Original DataFrame:")
print(df)
print("\nDataFrame after removing missing values:")
print(df_clean)
