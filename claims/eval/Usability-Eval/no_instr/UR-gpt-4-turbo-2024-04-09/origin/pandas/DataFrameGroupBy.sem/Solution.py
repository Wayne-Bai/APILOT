import pandas as pd

# Example DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [12, 14, None, 18, 17, 16]
}
df = pd.DataFrame(data)

# Compute the standard error of the mean for each group, excluding missing values
grouped_sem = df.groupby('Group')['Values'].sem()

print(grouped_sem)
