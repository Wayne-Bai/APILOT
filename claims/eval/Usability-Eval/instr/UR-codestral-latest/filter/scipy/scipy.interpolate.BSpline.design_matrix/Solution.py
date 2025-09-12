import numpy as np
from scipy.sparse import csr_matrix

# Assume this is your data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Creating design matrix
design_matrix = np.hstack((np.ones((data.shape[0], 1)), data))

# Convert the design matrix to csr_matrix
csr_design_matrix = csr_matrix(design_matrix)

print(csr_design_matrix)
