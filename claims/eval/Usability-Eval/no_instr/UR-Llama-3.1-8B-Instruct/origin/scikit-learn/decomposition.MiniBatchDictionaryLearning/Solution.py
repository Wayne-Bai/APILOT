# Import necessary modules from scikit-learn
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.datasets import make_blobs
from sklearn.preprocessing import normalize
import numpy as np
import matplotlib.pyplot as plt
from time import time

# Set the seed for reproducibility
np.random.seed(0)

# Generate a synthetic dataset
X, _ = make_blobs(n_samples=1000, n_features=100, centers=10, random_state=0)

# Normalize the data
X = normalize(X)

# Perform Mini-batch Dictionary Learning
d = 5  # Number of atoms in the dictionary
batch_size = 10  # Size of the mini-batch

mbdl = MiniBatchDictionaryLearning(n_components=d, batch_size=batch_size, alpha=1e-5, n_iter=500)
X_dict = mbdl.fit_transform(X)

# Plot the learned dictionary
fig, ax = plt.subplots(d, figsize=(4, 2*d))
for i in range(d):
    ax[i].imshow(X_dict[:, i].reshape((10, 10)).T, cmap='hu')
plt.show()
    
# Show the dictionary fit
plt.bar(range(d), mbdl.components_.ravel())
plt.title('Dictionary components')
plt.show()
