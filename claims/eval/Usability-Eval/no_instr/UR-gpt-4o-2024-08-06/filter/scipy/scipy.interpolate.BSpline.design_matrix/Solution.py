import numpy as np
from scipy.sparse import csr_matrix

def create_design_matrix(data):
    """
    Creates a design matrix in CSR format from the input data.
    
    Parameters:
    data (array-like): A 2D array or list of lists where each inner list represents a feature vector.
    
    Returns:
    scipy.sparse.csr_matrix: A design matrix in CSR format.
    """
    # Ensure the input data is a numpy array
    data_array = np.array(data)

    # Create a CSR format sparse matrix from the numpy array
    design_matrix = csr_matrix(data_array)

    return design_matrix

# Example usage:
data = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 1]
]

design_matrix = create_design_matrix(data)
print(design_matrix)
