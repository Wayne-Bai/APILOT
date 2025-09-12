# Import necessary libraries
from sklearn.base import BaseEstimator
from sklearn.decomposition import NMF
import numpy as np

# Function to perform Non-Negative Matrix Factorization (NMF)
def nmf(X, n_components):
    """
    Perform Non-Negative Matrix Factorization (NMF) on the given matrix X.

    Parameters:
    X (numpy array): Input matrix.
    n_components (int): Number of non-negative matrices to factor the input matrix into.

    Returns:
    W (numpy array): First non-negative matrix.
    H (numpy array): Second non-negative matrix.
    """
    # Create an instance of the NMF class
    nmf_model = NMF(n_components=n_components)

    # Fit the model to the data
    nmf_model.fit(X)

    # Get the non-negative matrices
    W = nmf_model.transform(X)
    H = nmf_model.components_

    return W, H

# Example usage
if __name__ == "__main__":
    # Create a sample matrix
    X = np.array([[1, 0, 0, 1],
                  [1, 0, 0, 1],
                  [0, 0, 1, 1]])

    # Perform NMF with 2 components
    n_components = 2
    W, H = nmf(X, n_components)

    print("First non-negative matrix W:")
    print(W)
    print("\nSecond non-negative matrix H:")
    print(H)
