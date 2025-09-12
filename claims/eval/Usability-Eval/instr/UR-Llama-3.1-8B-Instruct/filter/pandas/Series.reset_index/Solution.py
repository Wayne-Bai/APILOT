import pandas as pd

# Create a DataFrame with a specific index
index = pd.date_range('1/1/2022', periods=5)
data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data, index=index)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Reset the index
df_reset = df.reset_index()  # Resets the index and uses it as a column

# Print the new DataFrame
print("\n DataFrame after resetting the index:")
print(df_reset)
