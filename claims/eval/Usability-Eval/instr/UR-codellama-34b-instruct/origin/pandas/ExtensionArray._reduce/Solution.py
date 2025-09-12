import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# perform the reduction operation
result = df['A'].sum()

print(result) # output: 6
