
import pandas as pd

# Create a sample DataFrame
data = {'group': ['A', 'A', 'A', 'B', 'B', 'B'],
        'values': [10, 15, None, 20, 25, 30]}
df = pd.DataFrame(data)

# Compute standard error of the mean of groups, excluding missing values
sem_group = df.groupby('group')['values'].sem()
print(sem_group)
