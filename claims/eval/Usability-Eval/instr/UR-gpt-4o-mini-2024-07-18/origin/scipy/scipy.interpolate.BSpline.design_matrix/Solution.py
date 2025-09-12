import numpy as np
from scipy.sparse import csr_matrix

def design_matrix(X, interaction_only=False):
    n_samples, n_features = X.shape
    if interaction_only:
        # Create a list to hold the indexes of the non-zero interactions
        indices = []
        for i in range(n_features):
            for j in range(i + 1, n_features):
                indices.append((i, j))
        n_interactions = len(indices)
        data = np.ones(n_interactions)
        row_indices = np.zeros(n_interactions, dtype=int)
        col_indices = np.array(indices).flatten()
        return csr_matrix((data, (row_indices, col_indices)), shape=(n_samples, n_interactions))
    else:
        # Returning the original input as a CSR matrix
        return csr_matrix(X)

# Example usage
X = np.array([[1, 2], [3, 4], [5, 6]])
sparse_matrix = design_matrix(X, interaction_only=False)
print(sparse_matrix)
