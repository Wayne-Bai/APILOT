import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Values': [2, 3, 5, 7, 11, 13]
}

# Create DataFrame
df = pd.DataFrame(data)

# Group by 'Category' and compute the product of 'Values' for each group
result = df.groupby('Category')['Values'].prod().reset_index()

# Output the result
print(result)
