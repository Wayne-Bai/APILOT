import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

# Function to return index of first occurrence of minimum over requested axis
def idxmin_no_polyfit(df, axis=0):
    if axis == 0:
        return df.apply(lambda x: np.argmin(x.values))
    elif axis == 1:
        return df.apply(lambda x: x.idxmin(), axis=1)

# Print the original DataFrame
print("Original DataFrame:\n", df)

# Print the index of the first occurrence of the minimum value
print("\nIndex of first occurrence of minimum:")
print(idxmin_no_polyfit(df, axis=0))
