import pandas as pd

# Example DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Reset the index
df_reset_index = df.reset_index(drop=True)

print(df_reset_index)
