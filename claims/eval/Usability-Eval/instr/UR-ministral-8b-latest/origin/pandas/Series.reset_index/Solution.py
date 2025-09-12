import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

print("Original DataFrame:")
print(df)

# Reset index to generate a new DataFrame with reset index
df_reset = df.reset_index(drop=True)

print("\nDataFrame with Reset Index:")
print(df_reset)
