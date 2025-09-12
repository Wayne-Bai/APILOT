import pandas as pd

# Assuming df is your DataFrame. Replace this with your DataFrame name.
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': [9, 10, 11, 12]
})

# Use the dropna function to remove missing values.
df_clean = df.dropna()

# Print the DataFrame after removing missing values.
print(df_clean)
