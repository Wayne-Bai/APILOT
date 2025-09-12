import numpy as np
import scipy.linalg

# Create a Hermitian matrix
H = np.array([[1, 2 + 1j], [2 - 1j, 4]], dtype=complex)

# Compute the (Moore-Penrose) pseudo-inverse of the Hermitian matrix
pseudo_inverse = scipy.linalg.pinvh(H) # Note: pinv_working would be deprecated in future

print("Hermitian Matrix:")
print(H)
print("\nMoore-Penrose Pseudo-Inverse:")
print(np.real(pseudo_inverse))
