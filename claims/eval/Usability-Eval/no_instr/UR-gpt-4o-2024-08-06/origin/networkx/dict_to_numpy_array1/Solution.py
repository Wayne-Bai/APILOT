import networkx as nx
import numpy as np

def dict_to_1d_array(data_dict, mapping=None):
    # If a mapping is provided, map the keys to new values
    if mapping:
        data_dict = {mapping[key]: value for key, value in data_dict.items() if key in mapping}
    
    # Convert the dictionary values to a numpy 1D array
    result_array = np.array(list(data_dict.values()))
    
    return result_array

# Example usage
data = {1: 10, 2: 20, 3: 30}
mapping = {1: 'a', 2: 'b', 3: 'c'}
result = dict_to_1d_array(data, mapping)
print(result)
