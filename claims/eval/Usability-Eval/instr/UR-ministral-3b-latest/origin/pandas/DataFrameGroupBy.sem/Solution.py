
import pandas as pd

# Sample data
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, None, 3, 4, 5]
}

df = pd.DataFrame(data)

# Compute mean per group (excluding missing values)
grouped = df.groupby('A').apply(lambda x: x[['B', 'C']].mean().dropna())
grouped['Error'] = grouped.std() / (3 ** 0.5)

print(grouped)
