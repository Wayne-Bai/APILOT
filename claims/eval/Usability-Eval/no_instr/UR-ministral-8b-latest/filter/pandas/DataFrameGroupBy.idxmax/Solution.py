import pandas as pd

def find_first_occurrence_max_index(df, axis):
    if axis not in ['index', 'columns']:
        raise ValueError("Axis must be 'index' or 'columns'")

    if axis == 'index':
        max_value = df.idxmax(axis=0)
    else:
        max_value = df.idxmax(axis=1)

    column_wise_max = max_value.max()  # Determine the global maximum value
    index_of_max = max_value.idxmax(column_wise_max)
    return index_of_max
