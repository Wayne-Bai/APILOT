import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Assign desired index to the DataFrame
desired_index = ['row1', 'row2', 'row3']
df.index = desired_index

print(df)
