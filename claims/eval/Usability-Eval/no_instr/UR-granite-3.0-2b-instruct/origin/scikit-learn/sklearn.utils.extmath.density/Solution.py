from sklearn.preprocessing import LabelEncoder
import numpy as np

def compute_density(sparse_vector):
    # Convert sparse vector to dense vector
    dense_vector = np.array(sparse_vector)

    # Compute density
    density = np.sum(dense_vector) / len(dense_vector)

    return density

# Example usage
sparse_vector = [0, 0, 1, 0, 1, 0, 1, 0, 0, 1]
density = compute_density(sparse_vector)
print(f"The density of the sparse vector is: {density}")
