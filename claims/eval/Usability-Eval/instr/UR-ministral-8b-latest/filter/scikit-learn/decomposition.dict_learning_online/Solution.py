from sklearn.decomposition import TruncatedSVD
import numpy as np

def dictionary_learning(matrix, n_dictionary, seed=None):
    """
    Solves a dictionary learning matrix factorization problem online.

    Parameters:
    - matrix: A numpy 2D array (num_samples, num_features)
    - n_dictionary: An integer which is the desired dimensionality of the dictionary
    - seed: An integer for random seed

    Returns:
    - invented_features: The numpy 2D array of invented features
    - dictionary_matrix: The numpy 2D array of the dictionary
    """
    # Set the random seed for reproducibility
    np.random.seed(seed)

    # Get the initial number of samples and features
    num_samples, num_features = matrix.shape

    # Initialize the dictionary matrix with random values
    dictionary_matrix = np.random.rand(n_dictionary, num_features)

    for _ in range(1000):  # Iterate for a fixed number of times
        # Perform Truncated SVD to find the sparse approximation matrix
        # 'n_components' equals to `n_dictionary`
        svd = TruncatedSVD(n_components=n_dictionary)
        H = svd.fit_transform(matrix)

        # Perform Alternating Least Squares (ALS) to update the features and dictionary
        for i in range(num_samples):
            for j in range(n_dictionary):
                dictionary_matrix[j, :] = np.linalg.lstsq(H[i, j].reshape(-1, 1),
                                                           matrix[i, :].reshape(1, -1), rcond=None)[0]

    return dictionary_matrix, H

# Example usage
matrix = np.random.rand(100, 50)  # Replace with your data
n_dictionary = 20  # Example value
dictionary_matrix, invented_features = dictionary_learning(matrix, n_dictionary)
print("Dictionary Matrix: ", dictionary_matrix)
print("Invented Features: ", invented_features)
