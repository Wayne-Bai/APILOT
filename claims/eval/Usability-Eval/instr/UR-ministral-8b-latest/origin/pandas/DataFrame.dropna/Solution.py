import pandas as pd

# Sample DataFrame creation (for demonstration purpose)
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, 3, 4]
}
df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Remove missing values
df_cleaned = df.dropna()

# Display cleaned DataFrame
print("\nDataFrame after removing missing values:")
print(df_cleaned)
