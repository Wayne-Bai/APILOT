import pandas as pd

# Example DataFrame
data = {'A': [10, 20, 30, 40, 10],
        'B': [15, 20, 25, 10, 25],
        'C': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Function to get index of first occurrence of maximum over specified axis
def first_max_occurrence_index(df, axis=0):
    if axis == 0:
        max_index = df.idxmax()
        return list(max_index)
    elif axis == 1:
        max_index_series = df.idxmax(axis=df.index)
        return list(max_index_series.values)
    else:
        raise ValueError("Axis must be 0 or 1")

# Get index of the first occurrence of maximum values on columns
column_axis_index = first_max_occurrence_index(df, axis=1)
print(column_axis_index)
