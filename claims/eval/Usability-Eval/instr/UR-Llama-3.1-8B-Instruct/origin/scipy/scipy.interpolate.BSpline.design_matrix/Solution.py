from scipy.sparse import csr_matrix
import numpy as np

def design_matrix(feature_vectors, degree):
    """
    Returns a design matrix as a CSR format sparse array.

    Parameters:
    feature_vectors (2D numpy array): feature vectors
    degree (int): degree of the polynomial basis

    Returns:
    design_matrix (scipy.sparse.csr_matrix): CSR format sparse array design matrix
    """
    
    # Get the number of feature vectors
    N = feature_vectors.shape[0]
    
    # Initialize the design matrix with zeros
    design_matrix = csr_matrix(np.zeros((N, (degree+1)*feature_vectors.shape[1])))
    
    # Add 1's to the design matrix
    design_matrix[:, 0] = np.ones(N)
    
    # Add each feature in order
    for p in range(1, degree+1):
        for i in range(feature_vectors.shape[1]):
            column_index = i + p
            # Calculate the power of each feature and add to the design matrix
            design_matrix[:, column_index] = np.dot(np.power(feature_vectors, p), feature_vectors[:, i])
    
    return design_matrix

# Example usage
feature_vectors = np.array([[1., 2.], [2., 3.], [3., 4.], [4., 5.], [5., 6.], [6., 7.], [7., 8.]])
degree = 2

design_matrix = design_matrix(feature_vectors, degree)
print(design_matrix.toarray())
