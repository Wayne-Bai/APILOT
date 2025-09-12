# Import the necessary classes from scikit-learn
from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np

# Generate synthetic data for illustration
n_samples = 100
n_features = 50
n_components = 10
X = np.random.randn(n_samples, n_features)

# Instantiate the MiniBatchDictionaryLearning model
dict_learning = MiniBatchDictionaryLearning(n_components=n_components, alpha=1, n_iter=100, batch_size=10, random_state=0)

# Fit the model to the data
dictionary = dict_learning.fit(X)

# Transform the data into the new space using the dictionary learned
code = dict_learning.transform(X)

# Print the learned dictionary components and the transformed data
print("Dictionary Components:\n", dictionary.components_)
print("Transformed Data (Sparse Codes):\n", code)
