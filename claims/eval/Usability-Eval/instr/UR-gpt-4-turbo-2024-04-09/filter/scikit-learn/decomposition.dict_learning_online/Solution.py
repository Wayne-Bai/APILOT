import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Parameters
n_samples, n_features = 1000, 64  # Number of samples and features
n_components = 16  # Number of dictionary atoms to extract

# Generate synthetic data
np.random.seed(0)
data = np.random.rand(n_samples, n_features)

# Initialize the MiniBatchDictionaryLearning model
dict_learner = MiniBatchDictionaryLearning(n_components=n_components, alpha=0.1, n_iter=500)

# Fit the model
dictionary = dict_learner.fit(data)

# Extract the components (dictionary atoms)
components = dictionary.components_

# Output the dictionary atoms
print("Dictionary atoms:")
print(components)
