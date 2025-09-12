import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Assign desired index to the DataFrame
new_index = ['x', 'y', 'z']
df.index = new_index

print(df)
