import numpy as np

# Define the matrix
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], dtype='float32')

# Perform the QR factorization
q, r = np.linalg.qr(a)

# Print the results
print(f"Q: \n{q}\n")
print(f"R: \n{r}")
