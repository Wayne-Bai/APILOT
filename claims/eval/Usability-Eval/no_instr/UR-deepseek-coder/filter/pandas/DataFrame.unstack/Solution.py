import pandas as pd

# Sample DataFrame
data = {
    'A': ['one', 'one', 'two', 'two'],
    'B': ['a', 'b', 'a', 'b'],
    'C': [1, 2, 3, 4],
    'D': [10, 20, 30, 40]
}

df = pd.DataFrame(data)

# Pivot the DataFrame
pivot_df = df.pivot(index='A', columns='B', values=['C', 'D'])

print(pivot_df)
