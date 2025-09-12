
import pandas as pd

# Creating a sample dataframe
data = {
    'A': [1, 1, 1, 2, 2, 2],
    'B': ['X', 'X', 'Y', 'Y', 'Y', 'Z'],
    'C': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Pivot the dataframe
pivot_df = df.pivot(index='A', columns='B', values='C')

print(pivot_df)
