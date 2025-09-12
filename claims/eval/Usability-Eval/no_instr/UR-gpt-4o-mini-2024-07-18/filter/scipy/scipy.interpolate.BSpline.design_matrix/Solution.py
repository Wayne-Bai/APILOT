from scipy.sparse import csr_matrix
import numpy as np

def create_design_matrix(X):
    """
    Create a design matrix in CSR (Compressed Sparse Row) format 
    from the input array X.

    Parameters:
    X : array-like, shape (n_samples, n_features)
        Input data.

    Returns:
    csr_matrix
        Design matrix in CSR format.
    """
    # Convert the input array to a NumPy array if it's not already
    X_array = np.array(X)
    
    # Create a sparse matrix in CSR format
    design_matrix = csr_matrix(X_array)
    
    return design_matrix

# Example usage:
if __name__ == "__main__":
    data = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    csr_design_matrix = create_design_matrix(data)
    print(csr_design_matrix)
