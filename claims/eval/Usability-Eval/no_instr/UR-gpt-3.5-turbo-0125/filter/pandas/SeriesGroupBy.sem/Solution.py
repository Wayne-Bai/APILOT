
import pandas as pd

# Create a sample DataFrame for demonstration
data = {'group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'value': [10, 15, 20, None, 12, 18]}
df = pd.DataFrame(data)

# Compute standard error of the mean for each group, excluding missing values
sem_by_group = df.groupby('group')['value'].sem(skipna=True)
print(sem_by_group)
