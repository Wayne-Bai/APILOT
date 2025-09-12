import pandas as pd
data = {'group': ['A', 'A', 'A', 'B', 'B', 'B'],
 'score': [10, 20, None, 30, 40, 50]}
df = pd.DataFrame(data)
variance = df.groupby('group')['score'].var()
print(variance)
