import pandas as pd

# Sample data
data = {
    'A': ['foo', 'foo', 'bar', 'bar'],
    'B': [1, 2, 3, 4]
}

df = pd.DataFrame(data)

# Compute the product of group values
result = df.groupby('A')['B'].apply(lambda x: x.prod()).reset_index()

print(result)
