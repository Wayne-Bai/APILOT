import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [2, 3, 4, 5, 6, 7]
}

df = pd.DataFrame(data)

# Compute the product of values grouped by 'Group'
result = df.groupby('Group')['Values'].prod()

print(result)
