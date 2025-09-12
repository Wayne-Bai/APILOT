import pandas as pd
import numpy as np

def find_first_occurrence_of_min(iterable):
    """Return the first occurrence index of minimum over requested axis, excluding NA/null values."""
    iterable = pd.Series(iterable)
    iterable = iterable.where(~iterable.isnull(), float('inf'))
    return iterable.idxmin()

# Test the function
test_data = [5, np.nan, 3, 9, np.nan]
print(find_first_occurrence_of_min(test_data))
