import scipy.linalg as la
import numpy as np

# Create a Hermitian matrix
# A Hermitian matrix is a square matrix that is equal to its own conjugate transpose.
# In a real Hermitian matrix, the diagonal elements are real, 
# and the off-diagonal elements are symmetric.

# Here is an example of a Hermitian matrix
H = np.array([[4, 12 - 5j, 22 + 7j], 
              [12 + 5j, 37, 43 + 12j], 
              [22 - 7j, 43 - 12j, 91]])

# Compute the Moore-Penrose pseudo-inverse
# The np.linalg.pinv function uses Singular Value Decomposition (SVD) 
# to compute the pseudo-inverse of a matrix
pseudo_inverse = np.linalg.pinv(H)

# Verify the property of pseudo-inverse: A * A+ * A = A
# Where A is the Hermitian matrix, A+ is the pseudo-inverse of A
np.testing.assert_almost_equal(np.dot(H, pseudo_inverse).dot(H), H)

print(pseudo_inverse)
