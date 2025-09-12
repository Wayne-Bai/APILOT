import numpy as np
def arrays_any(array, axis=None):
    return np.any(array, axis=axis)

# Example usage
array = np.array([[False, False], [True, True]])
axis = 1
result = arrays_any(array, axis=axis)
print(result)
