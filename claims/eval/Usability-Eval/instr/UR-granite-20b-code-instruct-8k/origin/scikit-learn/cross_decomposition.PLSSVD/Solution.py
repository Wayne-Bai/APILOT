from sklearn.decomposition import PCA

X = ...  # Input data
n_components = ...  # Number of components to keep

pca = PCA(n_components=n_components)
X_reduced = pca.fit_transform(X)
