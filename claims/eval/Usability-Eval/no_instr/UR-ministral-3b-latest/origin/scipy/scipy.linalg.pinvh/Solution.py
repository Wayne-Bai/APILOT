import numpy as np
from scipy.linalg import pinv, hermitian
from scipy.sparse import csr_matrix

# Generating a random Hermitian matrix
A = np.random.rand(5, 5) + 1j * np.random.rand(5, 5)
A = (A + conj(A)) / 2  # Making it Hermitian

# Compute the Moore-Penrose pseudo-inverse
A_pseudo_inverse = pinv(A, sym_pos=True)

print(A_pseudo_inverse)
