
from sklearn.decomposition import PCA

# Assume 'X' is the transformed data to its reduced space using PCA

# Instantiate PCA with desired number of components
pca = PCA(n_components=2)

# Fit the PCA model on the transformed data 'X'
pca.fit(X)

# Transform the reduced data back to its original space
X_original = pca.inverse_transform(X)
