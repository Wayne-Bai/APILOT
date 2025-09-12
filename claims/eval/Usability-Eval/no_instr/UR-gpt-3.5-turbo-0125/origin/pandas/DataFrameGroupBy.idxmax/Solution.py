
import pandas as pd

# Create a sample DataFrame
data = {'A': [10, 20, 30, 40],
        'B': [50, 60, 70, 80],
        'C': [90, 100, 110, 120]
       }
df = pd.DataFrame(data)

# Find the index of the first occurrence of maximum value over the specified axis (0 - rows, 1 - columns)
index = df.idxmax(axis=0)
print(index)
