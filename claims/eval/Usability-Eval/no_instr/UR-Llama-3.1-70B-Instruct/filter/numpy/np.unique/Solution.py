import numpy as np

# Input array
arr = np.array([5, 2, 8, 1, 8, 5, 3, 7, 1, 2, 8, 9, 0])

# Find unique elements
unique_elements, indices, counts = np.unique(arr, return_index=True, return_counts=True)

print("Unique elements: ", unique_elements)
print("Indices of unique elements in the original array: ", indices)
print("Counts of unique elements in the original array: ", counts)

# Printing output in tabular form
print("\nTabular Output:")
for i, element in enumerate(unique_elements):
    print(f"Element: {element}, Index: {indices[i]}, Count: {counts[i]}")
