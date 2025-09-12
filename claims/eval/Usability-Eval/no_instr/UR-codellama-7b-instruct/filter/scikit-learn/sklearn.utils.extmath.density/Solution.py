
from sklearn.metrics import density
import numpy as np

# define a sparse vector
sparse_vector = np.array([1, 0, 2, 3, 0])

# compute the density of the sparse vector using the density function from scikit-learn
density = density(sparse_vector)

print(f"Density of the sparse vector: {density}")
