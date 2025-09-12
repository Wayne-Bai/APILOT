import pandas as pd

# Assume df is your original DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Reset the index of the DataFrame
df_reset = df.reset_index(drop=True)

# Display the new DataFrame with reset index
print(df_reset)
