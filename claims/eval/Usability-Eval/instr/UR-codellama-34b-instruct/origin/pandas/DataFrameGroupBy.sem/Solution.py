import pandas as pd

# Sample data
data = {'group': ['A', 'B', 'C'], 'value': [10, 20, 30]}
df = pd.DataFrame(data)

# Compute SEM for each group
sem = df.groupby('group')['value'].sem()
print(sem)
