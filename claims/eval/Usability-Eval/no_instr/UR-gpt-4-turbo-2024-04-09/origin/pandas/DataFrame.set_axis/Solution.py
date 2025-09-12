import pandas as pd

# Sample data in a DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}

df = pd.DataFrame(data)

# Assigning a new index to the DataFrame
new_index = ['x', 'y', 'z']
df.index = new_index

print(df)
