import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500],
}

df = pd.DataFrame(data)

grouped_df = df.groupby(['B'])['C'].sum().reset_index()

print(grouped_df)
