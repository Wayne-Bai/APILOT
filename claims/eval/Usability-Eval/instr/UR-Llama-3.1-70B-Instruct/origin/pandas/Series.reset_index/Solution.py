import pandas as pd

# Sample DataFrame
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "Country": ["USA", "UK", "Australia", "Germany"]
}

df = pd.DataFrame(data)

# Set Name as index
df = df.set_index('Name')

print("Original DataFrame:")
print(df)

# Reset index
df_reset = df.copy()  # Create a copy before resetting index
df_reset = df_reset._set_index_scoped(df_reset.columns, append=True, inplace=False).droplevel(-1, axis=0)

print("\nDataFrame with index reset:")
print(df_reset)
