import pandas as pd

# Creating a sample DataFrame
data = {'A': [4, 5, 1, 3], 'B': [10, 2, 7, 3]}
df = pd.DataFrame(data)

# Finding the index of the first occurrence of the minimum value over the default axis (axis=0)
index_of_min = df.idxmin()

print(index_of_min)
