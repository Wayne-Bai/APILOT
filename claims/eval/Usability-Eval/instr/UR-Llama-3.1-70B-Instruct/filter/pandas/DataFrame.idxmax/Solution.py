import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 4, 6, 8, 10]
})

# Find the index of the first occurrence of the maximum value in each column
max_indexes = df.apply(lambda x: np.argmax(x))

print(max_indexes)
