from sklearn.manifold import Isomap
import numpy as np

# Assume we have some data in a numpy array called 'data'
# data = np.array([...]) # replace [...'] with your array

# We need to choose the number of neighbors to consider for each point
n_neighbors = 5 # change this value according to your requirement

# Fit Isomap model
model = Isomap(n_neighbors = n_neighbors, n_components = 2) # we set the output dimension to be 2 for simplicity
embedding = model.fit_transform(data)

print('Shape of embedded data:', embedding.shape)
