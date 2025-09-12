import numpy as np
from sklearn.decomposition import PCA

# Assuming data is a centered numpy array of shape (n_samples, n_features)
data = ...

# Initialize PCA object
pca = PCA(n_components=0.95)  # Choose the number of components as 0.95 proportion of variance

# Fit and transform the data
data_pca = pca.fit_transform(data)

# Print the explained variance ratio for the chosen components
print("Explained variance ratio:", pca.explained_variance_ratio_)
