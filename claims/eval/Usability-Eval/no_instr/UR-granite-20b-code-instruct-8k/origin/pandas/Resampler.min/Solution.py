import pandas as pd
# create dataframe
data = {'Group': ['A', 'B', 'A', 'B'],
        'Value': [1, 2, 3, 4]}
df = pd.DataFrame(data)

# compute min value of group
min_value = df.groupby('Group')['Value'].min()

print(min_value)
