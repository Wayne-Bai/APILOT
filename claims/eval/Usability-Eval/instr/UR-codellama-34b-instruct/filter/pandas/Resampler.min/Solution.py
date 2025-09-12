import pandas as pd

# sample data
data = {'A': ['foo', 'bar', 'baz'],
        'B': [1, 2, 3],
        'C': [4, 5, 6]}
df = pd.DataFrame(data)

# group by column A and compute min of B
df_grouped = df.groupby('A')['B'].min()

# print the result
print(df_grouped)
