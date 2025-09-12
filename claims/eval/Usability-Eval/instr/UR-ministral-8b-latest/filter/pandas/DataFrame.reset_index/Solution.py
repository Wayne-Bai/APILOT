import pandas as pd

# Sample DataFrame with MultiIndex
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=[['a', 'a', 'b'], ['x', 'y', 'z']])

print("Original DataFrame:")
print(df)

# Reset the index of the DataFrame keeping the default index
df = df.reset_index(drop=True)

print("\nDataFrame after reset_index:")
print(df)
