import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

# Return index of first occurrence of maximum over requested axis
print("Index of first occurrence of maximum in each column:")
print(df.idxmax())

print("\nIndex of first occurrence of maximum in each row:")
print(df.idxmax(axis=1))
