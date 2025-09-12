
# Importing pandas library
import pandas as pd

# Assuming we have the following data:
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70, 80]
}

# Creating a DataFrame from the given data
df = pd.DataFrame(data)

# Computing the min value of each group
min_values = df.groupby('Group')['Value'].min()

# Printing the result
print(min_values)
