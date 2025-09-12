import scipy.sparse
import numpy as np

def generate_design_matrix(n_samples, n_features):
    """
    Returns a design matrix as a CSR format sparse array.

    Parameters:
    n_samples (int): Number of samples in the design matrix.
    n_features (int): Number of features in the design matrix.

    Returns:
    scipy.sparse.csr.csr_matrix: A design matrix in CSR format.
    """
    # Generate a random design matrix with 10% of the entries being non-zero
    data = np.random.rand(int(0.1 * n_samples * n_features))
    rows = np.random.randint(0, n_samples, size=len(data))
    cols = np.random.randint(0, n_features, size=len(data))

    # Create the design matrix as a CSR format sparse array
    design_matrix = scipy.sparse.csr_matrix((data, (rows, cols)), shape=(n_samples, n_features))

    return design_matrix

# Example usage:
n_samples = 1000
n_features = 100

design_matrix = generate_design_matrix(n_samples, n_features)

print("Design matrix shape:", design_matrix.shape)
print("Number of non-zero entries:", design_matrix.nnz)
print("Design matrix:")
print(design_matrix.toarray())
