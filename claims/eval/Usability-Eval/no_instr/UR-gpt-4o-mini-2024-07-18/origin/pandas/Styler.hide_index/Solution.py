import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

# Hide the entire index by converting to string representation without index
df_string = df.to_string(index=False)

# Hide specific index keys ('a' and 'b') from rendering
df_hidden_index = df.reset_index(drop=True)

print("DataFrame without index:")
print(df_string)

print("\nDataFrame with specific keys hidden:")
print(df_hidden_index)
