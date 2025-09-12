import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['index1', 'index2', 'index3'])

print("Original DataFrame:")
print(df)

# Hide the entire index
df_hidden = df.hidden(just_str=True).values

print("\nDataFrame after hiding the entire index:")
print(df_hidden)

# Hide specific keys in the index
df_specific = df.drop(index=['index2']).reset_index(drop=True)

print("\nDataFrame after hiding specific keys in the index:")
print(df_specific)
