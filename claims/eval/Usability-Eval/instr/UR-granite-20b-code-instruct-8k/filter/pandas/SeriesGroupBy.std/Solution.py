import pandas as pd
# Define a dataset
data = {'group': ['A', 'A', 'A', 'B', 'B', 'B'],
        'value': [1, 2, np.nan, 4, 5, np.nan]}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the standard deviation of groups, excluding missing values
result = df.groupby('group')['value'].std()

print(result)
