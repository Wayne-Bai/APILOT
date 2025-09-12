import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Reset the index
df_reset = df.reset_index(drop=True)

print(df_reset)
