
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# group the dataframe by column A and compute the product of values in column B
grouped_df = df.groupby('A')['B']
result = grouped_df.agg({'B': 'prod'})

print(result)
