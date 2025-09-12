import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 2, 3, 4, 4, 5],
    'B': [5, 4, 4, 3, 2, 2, 1]
})

# Remove duplicates based on index
df = df.set_index('A').drop_duplicates().reset_index(drop=True)

# If you want to remove duplicates based on the entire row, use:
# df = df.drop_duplicates()

print(df)
