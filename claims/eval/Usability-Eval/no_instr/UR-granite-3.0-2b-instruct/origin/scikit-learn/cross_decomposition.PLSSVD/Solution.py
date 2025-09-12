from sklearn.decomposition import TruncatedSVD

# Assuming X is your data matrix
svd = TruncatedSVD(n_components=2)  # Change n_components to your desired number of components
X_svd = svd.fit_transform(X)
