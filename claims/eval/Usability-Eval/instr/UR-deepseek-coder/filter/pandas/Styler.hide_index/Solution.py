import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Hide the entire index
df_hidden_index = df.style.hide(axis="index")

# Hide specific keys in the index
df_hidden_specific_index = df.style.hide(subset=[0, 2], axis="index")

# Display the DataFrames
print("DataFrame with hidden entire index:")
print(df_hidden_index.to_string())

print("\nDataFrame with hidden specific index keys:")
print(df_hidden_specific_index.to_string())
