import pandas as pd

# Sample DataFrame
data = {'Group': ['A', 'A', 'B', 'C', 'C', 'B', 'A']}
data['A'] = ['1', '2', None, '4', None, '6', '7']
data['B'] = [None, '1', '2', '3', '4', '5', None]
data['C'] = ['5', '6', None, None, '8', None, '9']

df = pd.DataFrame(data)

# Compute variance for each group, excluding NAN values
variance = df.groupby('Group').var()
print(variance)
