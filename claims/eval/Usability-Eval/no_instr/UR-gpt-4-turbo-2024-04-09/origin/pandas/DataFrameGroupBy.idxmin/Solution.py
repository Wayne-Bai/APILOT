import pandas as pd

# Sample DataFrame
data = pd.DataFrame({
    'A': [2, 3, 1, 4],
    'B': [5, 2, 3, 1],
    'C': [7, 8, 6, 5]
})

# Return index of first occurrence of minimum over requested axis
index_of_min = data.idxmin(axis=0)
print(index_of_min)
