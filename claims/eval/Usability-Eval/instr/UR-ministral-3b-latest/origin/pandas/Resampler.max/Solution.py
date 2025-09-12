import pandas as pd
data = {'A': [1, 2, 3, 4, 5],
        'B': [2, 7, 8, 9, 5],
        'C': [7, 8, 9, 1, 5]}

df = pd.DataFrame(data)
print(df)
max_values = df.groupby('A').max().transpose()
print(max_values)
