import numpy as np
from sklearn.decomposition import DictionaryLearning

# Set random seed for reproducibility
np.random.seed(0)

# Generate a synthetic dictionary matrix
n_components = 100  # Number of atoms in the dictionary
n_features = 5  # Number of features in each atom
n_samples = 50  # Number of samples in the dataset

# Create a random dictionary (atoms)
D = np.random.randn(n_components, n_features)

# Create a sparse code matrix
U_true = np.zeros((n_samples, n_components))
for i in range(n_samples):
    # Randomly select a few non-zero indices
    nnz_indices = np.random.choice(n_components, size=5, replace=False)
    # Assign random coefficients to these indices
    U_true[i, nnz_indices] = np.random.randn(5)

# Generate the signal
X = U_true @ D

# Perform dictionary learning
dict_learner = DictionaryLearning(n_components=n_components, alpha=1, max_iter=1000)
V = dict_learner.fit(X).components_

# Output the learned dictionary
print("Learned Dictionary (atoms):")
print(V)
