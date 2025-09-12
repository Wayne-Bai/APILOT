# Import pandas library
import pandas as pd

# Create a DataFrame with missing values
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [1, 2, None, 5, 6, 7]
}

df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
std_dev = df.groupby('Group')['Value'].agg(lambda x: x(sem=True), skipna=True)

print(std_dev)
