import numpy as np

def check_true_along_axis(arr, axis):
    return np.all(arr, axis=axis)

# Example usage
arr = np.array([[True, True], [True, False]])
axis = 0
result = check_true_along_axis(arr, axis)
print(result)  # Output depends on the array and the axis
