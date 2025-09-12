
from sklearn.decomposition import DictionaryLearning
import numpy as np

# Generate a random dataset for demonstration purposes
n_samples = 1000
n_features = 100
X = np.random.rand(n_samples, n_features)

# Define the mini-batch size and number of epochs
mini_batch_size = 10
n_epochs = 5

# Create a DictionaryLearning object with the specified parameters
dl = DictionaryLearning(n_components=20, alpha=0.1, n_jobs=-1)

# Fit the model to the data in mini-batches
for i in range(n_epochs):
    for j in range(0, n_samples, mini_batch_size):
        X_mb = X[j:j+mini_batch_size]
        dl.partial_fit(X_mb)

# Extract the learned dictionary and transform the data
W = dl.components_
X_transformed = W @ X.T
