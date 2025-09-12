import pandas as pd

# Creating a DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Computing the sum of group values
group_sum = df.groupby('Category')['Value'].sum().reset_index()

# Renaming the column
group_sum = group_sum.rename(columns={'Value': 'Sum_of_Value'})

# Displaying the result
print(group_sum)
