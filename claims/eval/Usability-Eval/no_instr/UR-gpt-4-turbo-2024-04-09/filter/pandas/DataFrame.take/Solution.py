import pandas as pd

data = {'Column1': [10, 20, 30, 40, 50],
        'Column2': [15, 25, 35, 45, 55],
        'Column3': [20, 30, 40, 50, 60]}

df = pd.DataFrame(data)

# Specify the indices you want to access
indices = [1, 3]

# Select rows by indices
result = df.iloc[indices]

print(result)
