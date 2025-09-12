import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Assign a new index to the DataFrame
new_index = ['row1', 'row2', 'row3']
df.index = new_index

print(df)
