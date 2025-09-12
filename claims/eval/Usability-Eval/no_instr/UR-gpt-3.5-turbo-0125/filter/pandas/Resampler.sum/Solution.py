
import pandas as pd

df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'B', 'C'],
    'value': [10, 20, 30, 15, 25, 5]
})

group_sum = df.groupby('group')['value'].sum()
print(group_sum)
