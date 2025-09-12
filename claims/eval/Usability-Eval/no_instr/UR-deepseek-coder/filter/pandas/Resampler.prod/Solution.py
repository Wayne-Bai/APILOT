import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [1, 2, 3, 4, 5, 6]
}

df = pd.DataFrame(data)

# Compute the product of group values
grouped_prod = df.groupby('Category')['Value'].prod().reset_index()

print(grouped_prod)
