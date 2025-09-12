import pandas as pd

# Let's assume we have the following DataFrame and we want to reset its index
df = pd.DataFrame({
   'A': ['A0', 'A1', 'A2'],
   'B': ['B0', 'B1', 'B2']
})

# Print the original DataFrame
print("Original DataFrame:\n", df)

# Reset the index and reset the index ID with -1
df_reset = df.reset_index(drop=True)

# Print the updated DataFrame
print("Updated DataFrame:\n", df_reset)
