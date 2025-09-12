import pandas as pd

# Assuming you have a DataFrame called df
df = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, None, 5],
    'C': [1, 2, 3, 4, None]
})

print("Original DataFrame:")
print(df)

# Use the dropna() function to remove missing values
df_clean = df.dropna()

print("\nDataFrame after removing missing values:")
print(df_clean)
