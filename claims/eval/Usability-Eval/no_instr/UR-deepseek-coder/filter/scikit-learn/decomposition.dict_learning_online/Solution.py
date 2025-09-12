import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Generate a synthetic dataset
n_samples = 1000
n_features = 50
n_components = 10

X = np.random.randn(n_samples, n_features)

# Initialize the MiniBatchDictionaryLearning model
dict_learner = MiniBatchDictionaryLearning(n_components=n_components, alpha=1, batch_size=3, n_iter=50)

# Fit the model to the data
dict_learner.fit(X)

# Transform the data to sparse representation
X_transformed = dict_learner.transform(X)

# The dictionary (D) and the sparse coefficients (X_transformed) are now available
dictionary = dict_learner.components_

print("Dictionary (D):")
print(dictionary)
print("Sparse coefficients (X_transformed):")
print(X_transformed)
