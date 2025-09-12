
from sklearn.decomposition import DictionaryLearning
import numpy as np

# Generate some sample data
X = np.random.rand(100, 10)

# Initialize the dictionary learning algorithm with the number of atoms and the regularization parameter
dl = DictionaryLearning(n_atoms=10, alpha=1e-3)

# Fit the data to the dictionary
dl.fit(X)

# Get the learned dictionary
dictionary = dl.components_
