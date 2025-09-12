import numpy as np

# Assume this is your dictionary of dictionaries
data = {
    'person1': {'age': 25, 'height': 180},
    'person2': {'age': 30, 'height': 175},
    # ...
}

# Extract keys from the first inner dictionary
keys = list(data[next(iter(data))].keys())

# Convert the dictionary of dictionaries to a list of lists
data_list = [[d[key] for key in keys] for d in data.values()]

# Convert the list of lists to a 2D NumPy array
array = np.array(data_list)
