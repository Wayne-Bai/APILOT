import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 5, 25, 7, 15]
}

df = pd.DataFrame(data)

# Compute the minimum value of each group
min_values = df.groupby('Category')['Value'].min().reset_index()

print(min_values)
