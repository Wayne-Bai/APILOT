
import numpy as np
from sklearn.decomposition import DictionaryLearning

# Create example data
X = np.random.rand(100, 20)

# Initialize the dictionary learning model
dl = DictionaryLearning(n_components=5)

# Fit the model to the data
dl.fit(X)

# Get the learned dictionary, each row represents an atom
dictionary = dl.components_
