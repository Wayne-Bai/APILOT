import numpy as np

def dict_to_1d_array(input_dict):
    # Check if the input is a dictionary
    if not isinstance(input_dict, dict):
        raise ValueError("Input should be a dictionary")

    # Convert the dictionary values to a list
    values_list = list(input_dict.values())

    # Convert the list to a numpy array
    array = np.array(values_list)

    return array

# Example usage:
input_dict = {'a': 1, 'b': 2, 'c': 3}
result_array = dict_to_1d_array(input_dict)
print(result_array)
