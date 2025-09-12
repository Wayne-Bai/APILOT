import pandas as pd

# Example data
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [2, 3, 5, 7, 11, 13]
}

df = pd.DataFrame(data)

# Compute the product of group values
result = df.groupby('Group')['Value'].prod()

print(result)
