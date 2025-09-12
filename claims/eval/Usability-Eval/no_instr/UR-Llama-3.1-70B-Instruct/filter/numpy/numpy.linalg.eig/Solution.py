import numpy as np

# Define a square array
A = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Print the eigenvalues
print("Eigenvalues: ", eigenvalues)

# Print the right eigenvectors
print("Right Eigenvectors:\n", eigenvectors)

# Verify that the equation Ax = λx holds true
for i in range(len(eigenvalues)):
    eigenvalue = eigenvalues[i]
    eigenvector = eigenvectors[:, i]
    
    # Calculate Ax
    Ax = np.dot(A, eigenvector)
    
    # Calculate λx
    lambdax = eigenvalue * eigenvector
    
    # Check if Ax is approximately equal to λx
    if np.allclose(Ax, lambdax):
        print(f"Verification passed for eigenvalue {eigenvalue} and eigenvector {eigenvector}")
    else:
        print(f"Verification failed for eigenvalue {eigenvalue} and eigenvector {eigenvector}")
