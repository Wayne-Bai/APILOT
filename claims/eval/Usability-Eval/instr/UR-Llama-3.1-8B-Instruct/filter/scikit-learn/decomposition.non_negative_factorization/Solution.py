# Importing the necessary libraries
from sklearn.decomposition import NMF
import numpy as np

# Function to perform NMF
def nmf(X, n_components):
    """
    Perform Non-Negative Matrix Factorization (NMF) on the input matrix X.

    Parameters:
    X (numpy array): Input matrix to be factorized.
    n_components (int): Number of components for the factorization.

    Returns:
    W (numpy array): Non-negative matrix whose columns are the basis vectors.
    H (numpy array): Non-negative matrix whose rows are the coefficients of the linear combination of the basis vectors.
    """
    # Initialize the NMF model
    nmf_model = NMF(n_components=n_components, init='random', random_state=0, max_iter=200)

    # Perform matrix factorization
    nmf_model.fit(X)

    # Get the non-negative matrices W and H from the model
    W = nmf_model.transform(X)
    H = nmf_model.components_

    return W, H

# Example usage
if __name__ == "__main__":
    # Randomly generate a 5x7 non-negative matrix
    X = np.random.rand(5, 7)

    # Set the number of components for the factorization
    n_components = 3

    # Perform NMF
    W, H = nmf(X, n_components)

    # Print the resulting matrices
    print("Matrix W:")
    print(W)
    print("\nMatrix H:")
    print(H)

    # To verify, let's check if W*H is close to X
    assert np.allclose(W @ H, X)
    print("\nW*H is close to X. NMF decomposition successful.")
