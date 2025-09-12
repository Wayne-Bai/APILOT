import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 5, 30, 2, 4]
}

df = pd.DataFrame(data)

# Group by 'Category' and compute the product of 'Value'
prod_values = df.groupby('Category')['Value'].prod().reset_index()

print(prod_values)
