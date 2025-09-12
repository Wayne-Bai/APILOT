
from sklearn.decomposition import DictionaryLearning
import numpy as np

# Generate some random data
n_samples, n_features = 100, 50
data = np.random.rand(n_samples, n_features)

# Initialize the dictionary learning module with the number of atoms
dict_learner = DictionaryLearning(n_atoms=10)

# Fit the data to the dictionary
dict_learner.fit(data)

# Print the learned dictionary
print(dict_learner.components_)
