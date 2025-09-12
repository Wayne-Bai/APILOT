import scipy.sparse as sp

def generate_design_matrix(n_samples, n_features):
    # Create a design matrix with ones on the diagonal and zeros elsewhere
    design_matrix = sp.lil_matrix((n_samples, n_features))
    for i in range(n_samples):
        design_matrix[i, i] = 1
    return design_matrix
