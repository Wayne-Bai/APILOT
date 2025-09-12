# Import necessary libraries
from sklearn.datasets import make_blobs
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.preprocessing import Normalizer
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
X, _ = make_blobs(500, 64, centers=64, random_state=1)

# Normalize the data
norm = Normalizer()
X = norm.fit_transform(X)

# Use Mini-Batch Dictionary Learning to find a dictionary
dict_learning = MiniBatchDictionaryLearning(n_components=64, 
                                            batch_size=100, 
                                            n_iter=100, 
                                            random_state=42)
dict_learning.fit(X)

# Get the learned dictionary
dictionary = dict_learning.components_

# Represent the data using the learned dictionary
data_points = dict_learning.transform(X)

# Print the learned dictionary
print(dictionary)

# Convert learned dictionary to image and display it
plt.gray()
plt.subplot(1, 2, 1)
plt.imshow(dictionary, aspect='auto')
plt.title("Learned Dictionary")
plt.subplot(1, 2, 2)
plt.hist(np.sum(dictionary, axis=1), bins=range(0, int(np.max(np.sum(dictionary, axis=1))) + 100))
plt.title("Total Variance of Dictionary Elements")
plt.show()
