import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compute_sparse_density(vector):
    """
    Compute the density of a sparse vector.

    The density of a sparse vector is defined as the ratio of the number of non-zero
    elements to the total number of elements.

    Parameters:
    vector (list or numpy array): A sparse vector represented as a list or numpy array.

    Returns:
    float: The density of the sparse vector.
    """
    # Convert the vector to a numpy array to enable efficient computations
    vector = np.array(vector)

    # Compute the total number of elements in the vector
    total_elements = len(vector)

    # Compute the number of non-zero elements in the vector
    non_zero_elements = np.count_nonzero(vector)

    # Compute the density of the sparse vector
    density = non_zero_elements / total_elements

    return density


def compute_sparse_density_alternative(vector):
    """
    Compute the density of a sparse vector using cosine similarity.

    This approach is based on the fact that the cosine similarity between a sparse
    vector and a dense vector of ones is equal to the density of the sparse vector.

    Parameters:
    vector (list or numpy array): A sparse vector represented as a list or numpy array.

    Returns:
    float: The density of the sparse vector.
    """
    # Convert the vector to a numpy array to enable efficient computations
    vector = np.array(vector)

    # Create a dense vector of ones with the same shape as the input vector
    dense_vector = np.ones_like(vector)

    # Compute the cosine similarity between the sparse vector and the dense vector
    similarity = cosine_similarity([vector], [dense_vector])[0][0]

    # The cosine similarity is equal to the density of the sparse vector
    density = similarity

    return density


# Example usage
sparse_vector = [0, 1, 0, 1, 0, 1, 1, 1]
density = compute_sparse_density(sparse_vector)
print("Density:", density)

density_alternative = compute_sparse_density_alternative(sparse_vector)
print("Density (alternative method):", density_alternative)
