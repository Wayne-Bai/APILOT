import networkx as nx

# Function to convert dictionary of dictionaries to a 2d numpy array with optional mapping
def dict_to_numpy(data, keys=None, values=None):
    # Check if data is a dictionary of dictionaries
    if not isinstance(data, dict) or not all(isinstance(v, dict) for v in data.values()):
        raise ValueError("Input data must be a dictionary of dictionaries")

    # Get the keys and values from the first dictionary in the hierarchy
    if keys is None:
        keys = list(data.keys())[0]
    if values is None:
        values = list(data[keys].keys())[0]

    # Initialize the numpy array
    num_rows = len(data[keys])
    num_cols = len(data[values])
    output = np.zeros((num_rows, num_cols))

    # Iterate over the dictionaries in the hierarchy
    for i, d1 in enumerate(data[keys]):
        for j, d2 in enumerate(data[values]):
            # Check if the key-value pair is present in any of the dictionaries
            if any(d1.get(key) == d2.get(value) for key, value in data[values][j].items()):
                output[i, j] = 1

    return output