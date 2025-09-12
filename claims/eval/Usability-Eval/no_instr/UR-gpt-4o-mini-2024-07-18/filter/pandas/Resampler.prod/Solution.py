import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [1, 2, 3, 4, 5, 6]
}

df = pd.DataFrame(data)

# Compute product of group values
result = df.groupby('Category')['Values'].prod().reset_index()

print(result)
