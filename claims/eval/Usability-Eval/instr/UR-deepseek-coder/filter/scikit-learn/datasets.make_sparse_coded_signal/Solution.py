import numpy as np
from sklearn.decomposition import DictionaryLearning

# Define the parameters
n_features = 100  # Number of features
n_components = 20  # Number of dictionary elements
n_samples = 50  # Number of samples
n_nonzero_coefs = 5  # Number of non-zero coefficients per sample

# Initialize the dictionary learning model
dict_learning = DictionaryLearning(n_components=n_components, transform_algorithm='omp', transform_n_nonzero_coefs=n_nonzero_coefs)

# Generate a random dictionary D
D = np.random.randn(n_features, n_components)

# Generate sparse coefficients X
X = np.zeros((n_components, n_samples))
for i in range(n_samples):
    # Randomly select n_nonzero_coefs indices
    nonzero_indices = np.random.choice(n_components, n_nonzero_coefs, replace=False)
    # Assign random values to these indices
    X[nonzero_indices, i] = np.random.randn(n_nonzero_coefs)

# Generate the signal Y = DX
Y = np.dot(D, X)

# Print the shapes and the generated signal
print("Shape of D:", D.shape)
print("Shape of X:", X.shape)
print("Shape of Y:", Y.shape)
print("Generated signal Y:\n", Y)
