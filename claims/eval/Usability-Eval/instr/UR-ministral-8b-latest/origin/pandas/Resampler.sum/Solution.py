import pandas as pd

# Example DataFrame
data = {'Groups': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Values': [10, 20, 30, 40, 50, 60]}

# Creating DataFrame
df = pd.DataFrame(data)

# Grouping by 'Groups' and computing the sum of 'Values'
grouped = df.groupby('Groups')['Values'].sum()

# Output the result
print(grouped)
