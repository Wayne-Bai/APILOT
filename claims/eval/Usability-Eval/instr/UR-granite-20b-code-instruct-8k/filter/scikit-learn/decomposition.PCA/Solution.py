from sklearn.decomposition import PCA

# assuming X is your input data
pca = PCA()
X_reduced = pca.fit_transform(X)
