import pandas as pd

# Create a sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# Group by 'Group' and compute the product of 'Value'
group_prod = df.groupby('Group')['Value'].prod()

print(group_prod)
