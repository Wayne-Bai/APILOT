import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [4, 3, 2, 1],
    'C': [1, 3, 2, 4]
}
df = pd.DataFrame(data)

# Get the index of the first occurrence of the maximum value over the specified axis
# Using axis=0 to get the index of the first occurrence of the maximum for each column
max_index = df.idxmax(axis=0)

print(max_index)
