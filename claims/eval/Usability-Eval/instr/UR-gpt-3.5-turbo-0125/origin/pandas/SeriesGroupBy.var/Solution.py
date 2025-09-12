
import pandas as pd

data = {'group': ['A', 'A', 'B', 'B', 'B', 'A'],
        'value': [10, 7, 5, None, 8, 12]}

df = pd.DataFrame(data)

grouped = df.groupby('group')['value']
variance = grouped.apply(lambda x: x.dropna().var())

print(variance)
