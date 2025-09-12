import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
   'Group': ['A', 'A', 'B', 'B', 'A'],
   'Value': [10, 20, 30, 15, 5]
})

# Compute min value of group
min_values = df.groupby('Group')['Value'].min()

print(min_values)
