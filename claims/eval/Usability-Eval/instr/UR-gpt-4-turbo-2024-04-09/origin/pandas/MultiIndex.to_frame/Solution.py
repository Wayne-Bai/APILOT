import pandas as pd

# Creating a sample DataFrame with a MultiIndex
index = pd.MultiIndex.from_product([['A', 'B'], [1, 2]], names=['Letter', 'Number'])
data = {'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data, index=index)

# Reset index to convert MultiIndex into columns
df_reset = df.reset_index()

print(df_reset)
