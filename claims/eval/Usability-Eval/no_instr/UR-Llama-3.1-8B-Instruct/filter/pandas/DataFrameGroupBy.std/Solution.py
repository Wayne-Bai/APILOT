# Import the pandas library
import pandas as pd

# Create a sample dataframe
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 15, None, 20, 25, None, 30, 35, 40]
}
df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
std_dev = df.groupby('Group')['Value'].skipmissing().std()

print(std_dev)
