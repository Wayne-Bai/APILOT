
import numpy as np
from scipy.sparse import csr_matrix

# Define the shape of the matrix
n_rows = 10
n_cols = 5

# Initialize an empty CSR array with zeros
array = csr_matrix((n_rows, n_cols))

# Fill the array with data
for i in range(n_rows):
    for j in range(n_cols):
        array[i, j] = 1 / (i + 1)

print(array.todense())
