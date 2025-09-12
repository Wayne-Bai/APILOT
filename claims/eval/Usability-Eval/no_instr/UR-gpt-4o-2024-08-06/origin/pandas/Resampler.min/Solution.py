import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 15, 10, 5, 20, 25]
}

df = pd.DataFrame(data)

# Compute the minimum value for each group in 'Category'
min_values = df.groupby('Category')['Value'].min().reset_index()

print(min_values)
