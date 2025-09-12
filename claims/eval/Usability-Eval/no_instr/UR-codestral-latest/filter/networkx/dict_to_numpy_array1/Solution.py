import numpy as np
import pandas as pd

# Assume the dictionary is as follows:
dict_numbers = {'key1': 1, 'key2': 2, 'key3': 3}

# Convert the dictionary to a pandas Series, which can then be converted to a numpy array
np_array = pd.Series(dict_numbers).values

print(np_array)
