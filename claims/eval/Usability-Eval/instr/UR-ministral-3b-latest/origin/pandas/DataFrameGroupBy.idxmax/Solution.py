import pandas as pd

# Assuming you have a DataFrame 'df'
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
})

# Creating function to find the index of the first occurrence of maximum value along the requested axis
def first_occurrence_of_max_index(df, axis):
    if axis not in [0, 1]:  # Check if axis is valid
        raise ValueError("Axis should be either 0 (rows) or 1 (columns)")

    max_index = df.idxmax() if axis == 0 else df.idxmax(axis=1)

    return max_index

df
