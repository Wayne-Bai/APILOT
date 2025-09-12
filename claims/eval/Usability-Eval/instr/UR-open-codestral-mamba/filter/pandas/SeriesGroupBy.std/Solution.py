import pandas as pd

# Assuming you have a DataFrame 'df' with a column 'group' specifying the group and 'values' specifying the values
# Replace 'df', 'group', and 'values' with your actual DataFrame and column names

df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'B', 'A', 'A', 'B'],
    'values': [1, 2, 3, None, 5, None, 7, 8],
})

# Compute the standard deviation of each group, excluding missing values
std_dev = df.groupby('group')['values'].apply(lambda x: x.dropna().std())

print(std_dev)
