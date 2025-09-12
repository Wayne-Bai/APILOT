# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 15, 7, 12, 20, 25]
}
df = pd.DataFrame(data)

# Group by 'Group' and calculate the sum of 'Value'
group_sum = df.groupby('Group')['Value'].sum()

# Print the result
print(group_sum)
