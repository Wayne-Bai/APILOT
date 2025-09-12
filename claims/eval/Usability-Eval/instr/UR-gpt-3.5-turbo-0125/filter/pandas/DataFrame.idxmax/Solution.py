
import pandas as pd

# Creating a sample DataFrame
data = {'A': [10, 20, 30, 40],
        'B': [15, 25, 35, 45],
        'C': [25, 35, 45, 55]}

df = pd.DataFrame(data)

# Function to find index of first occurrence of maximum value along the given axis
def idxmax_custom(df, axis):
    if axis == 0:
        return df.idxmax(axis=axis).idxmax()
    elif axis == 1:
        return df.idxmax(axis=axis).idxmax()

# Call the function to retrieve the index of first occurrence of maximum over the requested axis
index_max_col = idxmax_custom(df, axis=0)
index_max_row = idxmax_custom(df, axis=1)

print("Index of first occurrence of maximum value along columns:", index_max_col)
print("Index of first occurrence of maximum value along rows:", index_max_row)
