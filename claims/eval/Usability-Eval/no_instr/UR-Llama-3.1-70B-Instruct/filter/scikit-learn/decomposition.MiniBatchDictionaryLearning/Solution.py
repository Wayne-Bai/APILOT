# Import necessary libraries
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.datasets import load_digits
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import MiniBatchKMeans
import numpy as np
import matplotlib.pyplot as plt

# Load the Digits dataset
digits = load_digits(n_class=6)

# Define the parameters
nrows, ncols = 8, 8
n_components = 64
image_array = np.reshape(digits.data[:n_components], (n_components, nrows, ncols))

# Create a graph of 8x8 images
graph = grid_to_graph(nrows, ncols)

# Define features for the MiniBatchDictionaryLearning function
X = digits.data

# Create an instance of the MiniBatchDictionaryLearning class
dico = MiniBatchDictionaryLearning(n_components=n_components, alpha=1, n_iter=50)

# Fit the model to the data
V = dico.fit_transform(X)

# From the n_components features learnt by MiniBatchDictionaryLearning 
# reconstruct center from the condensed version of center
dictionary_compact = dico.components_.reshape((n_components, nrows, ncols))

# Define the parameters and create an instance of the MiniBatchKMeans class
kmeans = MiniBatchKMeans(n_clusters=n_components, random_state=0, batch_size=3)

# Fit the model to the data
kmeans.fit(X)

# From center, normalise and de-normalise back features learnt by MiniBatchKMeans
features_compact_kmeans = kmeans.cluster_centers_

# Check learnt MiniBatchDictionaryLearning shape size is equal to MiniBatchKMeans
assert dictionary_compact.shape == features_compact_kmeans.shape

# Check the reconstructed features between two models
plt.figure(figsize=(16,6))

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(dictionary_compact[i], interpolation='nearest')
    plt.title('dictionary_compact[%d]' % i)

plt.show()

# Check difference of reconstructed center beween two methods
plt.figure(figsize=(16,6))

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(features_compact_kmeans[i], interpolation='nearest')
    plt.title('features_compact_kmeans[%d]' % i)

plt.show()
