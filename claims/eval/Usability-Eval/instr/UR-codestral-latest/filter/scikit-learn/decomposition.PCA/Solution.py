# Importing the required library
from sklearn.decomposition import PCA
import numpy as np

# Assuming `data` is your input data as a numpy array
# Center the data
data_centered = data - np.mean(data, axis=0)

# Create a PCA object
pca = PCA()

# Perform SVD and transform data to lower dimensional space
data_pca = pca.fit_transform(data_centered)
