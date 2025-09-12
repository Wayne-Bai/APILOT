import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Assign desired index to the given axis (e.g., axis=0 for rows)
desired_index = ['row1', 'row2', 'row3']
df.index = desired_index

# Assign desired columns to the given axis (e.g., axis=1 for columns)
desired_columns = ['colA', 'colB', 'colC']
df.columns = desired_columns

print(df)
