import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'B', 'A', 'A'],
    'Values': [1, 2, 3, 4, 5, 6, 7]
})

# Group the DataFrame by 'Group' and compute the sum of 'Values'
group_sum = df.groupby('Group')['Values'].sum()
print(group_sum)
