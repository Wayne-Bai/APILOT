import numpy as np
from sklearn.preprocessing import normalize

# Example sparse vector represented as a dictionary
sparse_vector = {0: 3, 2: 1, 4: 2}

# Convert the sparse vector to a dense numpy array
dense_vector = np.zeros(max(sparse_vector.keys()) + 1)
for key, value in sparse_vector.items():
    dense_vector[key] = value

# Compute the density of the vector
density = np.count_nonzero(dense_vector) / len(dense_vector)

print(f"Density of the sparse vector: {density}")
