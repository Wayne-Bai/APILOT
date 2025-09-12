# Import necessary libraries from scikit-learn
from sklearn.decomposition import NMF

# Import numpy for matrix operations
import numpy as np

# Function to perform NMF
def perform_nmfa(X, n_components):
    """
    Perform Non-Negative Matrix Factorization (NMF) to factorize a matrix X into W and H.
    
    Parameters:
    X (numpy array): Input matrix.
    n_components (int): Number of components in the reduced space.
    
    Returns:
    W (numpy array): Non-negative matrix.
    H (numpy array): Non-negative matrix.
    """
    # Initialize NMF model
    nmf_model = NMF(n_components=n_components, init='random', random_state=0)

    # Fit the model to the data
    W = nmf_model.fit_transform(X)

    # Get the coefficients
    H = nmf_model.components_

    return W, H

# Create a sample matrix
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Perform NMF
n_components = 2  # Choose the desired number of components
W, H = perform_nmfa(X, n_components)

print("Matrix X:")
print(X)
print("Matrix W:")
print(W)
print("Matrix H:")
print(H)
