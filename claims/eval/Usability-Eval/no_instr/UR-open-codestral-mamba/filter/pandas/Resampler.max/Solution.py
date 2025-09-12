# Importing pandas
import pandas as pd

# Let's assume we have a DataFrame df with the following data
# df has columns 'Group' and 'Value'
df = pd.DataFrame({
   'Group': ['A', 'A', 'B', 'B', 'A', 'B', 'B'],
   'Value': [10, 20, 30, 40, 50, 60, 70]
})

# Compute max value of group
max_values = df.groupby('Group')['Value'].max()

print(max_values)
