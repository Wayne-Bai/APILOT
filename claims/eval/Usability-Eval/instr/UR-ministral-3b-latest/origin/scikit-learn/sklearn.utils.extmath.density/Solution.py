from scipy.special import gamma
import numpy as np

def compute_density(X):
    # Convert sparse matrix to dense matrix for computational purposes
    dense_X = np.asarray(X.todense())

    # Calculate the gamma function for each element in the dense matrix
    gamma_values = gamma(1 + np.abs(dense_X))

    # Compute the density of each element in the sparse vector
    density = np.squeeze(gamma_values / gamma(1 + np.reciprocal(np.abs(dense_X))))

    return density
