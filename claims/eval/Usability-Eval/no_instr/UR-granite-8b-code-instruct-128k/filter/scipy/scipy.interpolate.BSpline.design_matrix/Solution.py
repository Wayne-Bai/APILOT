from scipy.sparse import csr_matrix
def generate_design_matrix(X):
    # Generate a design matrix from the input array X
    n_samples, n_features = X.shape
    # Create an empty CSR matrix with the correct shape
    design_matrix = csr_matrix((n_samples, n_features))
    # Populate the CSR matrix with the input data
    for i in range(n_samples):
        for j in range(n_features):
            design_matrix[i, j] = X[i, j]
    return design_matrix
