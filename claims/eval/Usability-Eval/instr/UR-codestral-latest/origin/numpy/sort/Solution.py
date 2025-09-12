import numpy as np

def sort_array(array):
    return np.sort(array, axis=None)

# test the function with an example
example_array = np.array([3,1,2,5,4])
sorted_array = sort_array(example_array)
print(sorted_array)
