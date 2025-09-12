import pandas as pd

# create a dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [2, 3, 4, 5, 6],
                   'C': [3, 4, 5, 6, 7]})

# define the quantile
q = 0.75

# calculate the quantile for each group
grouped = df.groupby('A')
result = grouped.quantile(q)

print(result)
