import pandas as pd

# Create a sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Group by 'Category' and compute the sum of 'Value'
grouped = df.groupby('Category')['Value'].sum()

print(grouped)
