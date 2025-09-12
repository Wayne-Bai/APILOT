from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np

# Let's assume we have a matrix X that we want to factorize
# X is a 2D array of shape (n_samples, n_features)
X = np.random.rand(100, 100)

# Create a dictionary learning object and transform the data
dict_learner = MiniBatchDictionaryLearning(n_components=10, alpha=1, n_iter=500)
code = dict_learner.fit_transform(X)

# `code` now contains the sparse codes that describe each sample as a sparse linear combination of the dictionary atoms
# `dict_learner.components_` now contains the dictionary atoms
