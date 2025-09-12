# Import necessary libraries
from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np

# Create a random dataset (for example a 1000 samples with 1000 features)
np.random.seed(0)
X = np.random.rand(1000, 1000)

# Create a dictionary learning object with 10 mini-batches and 1000 iterations
dico = MiniBatchDictionaryLearning(n_components=100, batch_size=10, alpha=0.1, n_iter=1000, random_state=0)

# Fit the data to the dictionary learning object
dico.fit(X)

# Get the learned dictionary
dictionary = dico.components_

# Get the learnt representation (coefficient) of the data with respect to the dictionary
representation = dico.transform(X)

# Print the results
print("Learned dictionary shape:", dictionary.shape)
print("Learned representation shape:", representation.shape)

# You can also get the partial fit to train the model in an online manner
# For example to train it in 3 partial fits
dico.partial_fit(X[:100])
dico.partial_fit(X[100:200])
dico.partial_fit(X[200:])

print("Learned dictionary after online learning shape:", dico.components_.shape)
