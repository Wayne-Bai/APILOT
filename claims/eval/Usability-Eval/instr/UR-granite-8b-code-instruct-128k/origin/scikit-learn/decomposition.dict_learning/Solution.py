
import numpy as np
from sklearn.decomposition import DictionaryLearning

# Generate a random matrix to factorize
X = np.random.rand(100, 1000)

# Initialize the DictionaryLearning object
dl = DictionaryLearning(n_components=100, alpha=1, random_state=0)

# Fit the dictionary learning model to the data
dl.fit(X)

# Print the learned dictionary
print(dl.components_)
