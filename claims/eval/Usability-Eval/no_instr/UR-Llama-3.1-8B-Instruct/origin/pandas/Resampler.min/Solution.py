# Import necessary library
import pandas as pd

# Create a sample DataFrame
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 15, 7, 20, 12, 7, 18, 25]
}
df = pd.DataFrame(data)

# Group by 'Group' and compute the minimum value of each group
min_values = df.groupby('Group')['Value'].min()

# Print the result
print(min_values)
