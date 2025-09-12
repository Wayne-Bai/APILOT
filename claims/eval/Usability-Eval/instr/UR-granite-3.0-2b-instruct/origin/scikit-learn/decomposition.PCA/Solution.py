from sklearn.decomposition import PCA

# Assuming X is your input data with shape (n_samples, n_features)
pca = PCA()
X_pca = pca.fit_transform(X)
