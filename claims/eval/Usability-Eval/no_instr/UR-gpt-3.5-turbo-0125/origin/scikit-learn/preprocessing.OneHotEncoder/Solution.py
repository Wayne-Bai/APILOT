
import numpy as np

def one_hot_encode(X):
    unique_values = np.unique(X)
    encoded_array = np.zeros((len(X), len(unique_values)))
    for i, value in enumerate(X):
        index = np.where(unique_values == value)[0][0]
        encoded_array[i][index] = 1
    return encoded_array

# Example usage
X = np.array(['A', 'B', 'A', 'C', 'B'])
encoded_X = one_hot_encode(X)
print(encoded_X)
