from sklearn.decomposition import PCA

# Assume X is the original data and pca is the PCA object
# X = ...
# pca = PCA(n_components=n_features)
# X_transformed = pca.fit_transform(X)

# To inverse the transformation
X_inverted = pca.inverse_transform(X_transformed)
