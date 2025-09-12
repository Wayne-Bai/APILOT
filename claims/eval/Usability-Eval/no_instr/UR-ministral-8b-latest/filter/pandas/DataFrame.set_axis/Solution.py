import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}
df = pd.DataFrame(data)

# Assigning Index to 'B' column
df.index = df['B']

# Drop the 'B' column if it's no longer needed
df = df.drop(columns=['B'])

print(df)
