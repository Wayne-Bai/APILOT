import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Generate random data
n_samples = 100
n_features = 10
X = np.random.rand(n_samples, n_features)

# Set parameters
n_components = 5
alpha = 1
batch_size = 3
n_iter = 10

# Perform Mini-batch dictionary learning
dico = MiniBatchDictionaryLearning(n_components=n_components, alpha=alpha, batch_size=batch_size, n_iter=n_iter)
dictionary = dico.fit(X).components_
