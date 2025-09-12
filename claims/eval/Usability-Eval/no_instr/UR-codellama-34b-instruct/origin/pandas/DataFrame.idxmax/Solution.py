import pandas as pd

def get_first_max_index(data, axis):
    """Return the index of the first occurrence of the maximum value over a given axis."""
    # Get the maximum value along the requested axis
    max_value = data.max(axis=axis)

    # Find the first occurrence of the maximum value
    first_occurrence = data[data == max_value].index.get_level_values(0).item()

    return first_occurrence
