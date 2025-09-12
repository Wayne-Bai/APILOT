import pandas as pd

# Assuming df is your DataFrame and 'axis' is either 'rows' or 'columns'
axis = 'rows'  # or 'columns'
indices = [0, 2, 4]  # replace with your desired indices

if axis == 'rows':
    result = df.iloc[indices]
else:
    result = df.iloc[:, indices]

print(result)
