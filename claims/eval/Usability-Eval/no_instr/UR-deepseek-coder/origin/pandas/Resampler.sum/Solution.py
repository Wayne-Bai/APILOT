import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 15, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

# Compute sum of group values
grouped_sum = df.groupby('Category')['Value'].sum().reset_index()

print(grouped_sum)
