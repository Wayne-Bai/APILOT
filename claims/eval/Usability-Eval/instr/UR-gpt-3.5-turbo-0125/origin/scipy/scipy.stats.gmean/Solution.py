
import numpy as np

def weighted_geometric_mean(data, weights, axis=None):
    if axis is None:
        product = np.prod(data ** weights)
        return product ** (1 / np.sum(weights))
    else:
        if len(weights) != data.shape[axis]:
            raise ValueError("Length of weights should match the length of data along the specified axis")
        
        weighted_data = data ** weights
        product = np.prod(weighted_data, axis=axis)
        return product ** (1 / np.sum(weights))

# Example usage:
data = np.array([[2, 3, 4], [5, 6, 7]])
weights = np.array([0.2, 0.3, 0.5])
result = weighted_geometric_mean(data, weights, axis=1)
print(result)
