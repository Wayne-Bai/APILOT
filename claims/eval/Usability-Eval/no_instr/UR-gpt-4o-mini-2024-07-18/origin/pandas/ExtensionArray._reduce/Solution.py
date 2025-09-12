import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}
df = pd.DataFrame(data)

# Perform a reduction operation, for example, calculating the sum of column 'A'
result = df['A'].sum()

# Return the scalar result
print(result)
