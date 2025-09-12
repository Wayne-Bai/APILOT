import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 2, 3, 4, 4, 4], 'B': [5, 6, 6, 7, 8, 8, 8]}
df = pd.DataFrame(data)

# Remove duplicate values
deduplicated_df = df.drop_duplicates()

print(deduplicated_df)
