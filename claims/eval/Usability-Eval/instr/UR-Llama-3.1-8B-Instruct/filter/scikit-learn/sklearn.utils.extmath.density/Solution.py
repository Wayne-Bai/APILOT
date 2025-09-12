# Import the necessary module from scikit-learn for computing density of a sparse vector
from scipy.sparse import csr_matrix
from scipy.sparse import issparse
import numpy as np

# Function to compute density of a sparse vector
def compute_density(vector):
    """
    Compute density of a sparse vector.

    Parameters:
    vector (list or numpy array): The input vector

    Returns:
    float: The density of the input vector
    """
    # Convert the input vector to a csr_matrix if it's not already sparse
    if not issparse(vector):
        vector = csr_matrix(vector)

    # Get the number of non-zero elements and the total number of elements
    num_non_zero = vector.count_nonzero()
    total_elements = vector.shape[0] * vector.shape[1]

    # Ensure total elements are known if the vector is a 1-D array, 
    # in which case, this value is the vector's length instead.
    total_elements = total_elements if vector.ndim > 1 else vector.shape[0]
    
    # Compute the density of the sparse vector
    density = num_non_zero / total_elements

    return density

# Example usage
vector = np.array([0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 0])
print("Density of the sparse vector: ", compute_density(vector))
