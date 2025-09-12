import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.preprocessing import normalize

# Parameters
n_samples = 100  # number of samples
n_components = 15  # number of dictionary elements/components
n_features = 64  # features per sample
n_nonzero_coefs = 5  # sparsity (number of nonzero coefficients)

# Generate a synthetic dataset
np.random.seed(42)
data = np.random.randn(n_samples, n_features)

# Normalize data
data = normalize(data)

# Initialize dictionary learning
dict_learner = MiniBatchDictionaryLearning(n_components=n_components, alpha=1, n_iter=500)

# Fit to data
V = dict_learner.fit(data).components_

# Generate sparse codes
sparse_codes = np.zeros((n_samples, n_components))
for i in range(n_samples):
    idx = np.random.choice(n_components, n_nonzero_coefs, replace=False)
    sparse_codes[i, idx] = np.random.randn(n_nonzero_coefs)

# Generate the signal
generated_signals = np.dot(sparse_codes, V)

print("Generated signals shape:", generated_signals.shape)
print("Dictionary shape:", V.shape)
