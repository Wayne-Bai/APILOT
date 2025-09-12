from scipy.sparse import csr_matrix
import numpy as np

# Assuming X is your data
X = np.array([[1, 2, 0], [3, 4, 5], [0, 6, 7]])

# Create a design matrix
design_matrix = csr_matrix(X)

print(design_matrix)
