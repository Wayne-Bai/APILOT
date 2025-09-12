import numpy as np

def find_unique_elements(array):
    unique_elements, indices, counts = np.unique(array, return_index=True, return_counts=True)
    return unique_elements, indices, counts

# Example usage
array = np.array([1, 2, 2, 3, 4, 4, 5, 5, 5])
unique_elements, indices, counts = find_unique_elements(array)

print("Unique Elements:")
print(unique_elements)
print("Indices:")
print(indices)
print("Counts:")
print(counts)
