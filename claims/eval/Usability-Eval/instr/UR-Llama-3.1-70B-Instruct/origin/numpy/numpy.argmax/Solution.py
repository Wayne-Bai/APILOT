import numpy as np

def get_max_indices(arr, axis=0):
    """
    Returns the indices of the maximum values along an axis.

    Parameters:
    arr (numpy.ndarray): Input array.
    axis (int, optional): Axis along which to find the maximum values. Defaults to 0.

    Returns:
    numpy.ndarray: Indices of the maximum values along the specified axis.
    """
    # Get the shape of the input array
    shape = arr.shape
    
    # Initialize an empty list to store the indices
    indices = []
    
    # If axis is 0, find the indices of maximum values along the columns
    if axis == 0:
        for i in range(shape[1]):
            max_val = np.max(arr[:, i])
            for j in range(shape[0]):
                if arr[j, i] == max_val:
                    indices.append(j)
                    break
    # If axis is 1, find the indices of maximum values along the rows
    elif axis == 1:
        for i in range(shape[0]):
            max_val = np.max(arr[i, :])
            for j in range(shape[1]):
                if arr[i, j] == max_val:
                    indices.append(j)
                    break
    
    # Return the indices as a numpy array
    return np.array(indices)

# Example usage
arr = np.array([[1, 3, 2], [4, 6, 5], [7, 9, 8]])
print("Input array:")
print(arr)

print("\nIndices of maximum values along axis 0:")
print(get_max_indices(arr, axis=0))

print("\nIndices of maximum values along axis 1:")
print(get_max_indices(arr, axis=1))
