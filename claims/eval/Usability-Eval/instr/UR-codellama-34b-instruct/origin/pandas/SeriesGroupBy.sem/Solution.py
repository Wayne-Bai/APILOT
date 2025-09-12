import pandas as pd

# Sample data
data = {'group': ['A', 'A', 'B', 'B', 'C', 'C'], 
        'value': [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)

# Compute standard error of the mean for each group
std_error = df.groupby('group').value.mean().sem()
print(std_error)
