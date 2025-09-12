import numpy as np
from sklearn.utils.extmath import density

# Create a sparse vector using a NumPy array
sparse_vector = np.array([0, 0, 1, 0, 0, 2, 0, 0, 3])

# Compute the density of the sparse vector
vector_density = density(sparse_vector)

print("Density of the sparse vector:", vector_density)
