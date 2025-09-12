import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 15, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

# Compute the min value of each group
min_values = df.groupby('Category')['Value'].min()

print(min_values)
