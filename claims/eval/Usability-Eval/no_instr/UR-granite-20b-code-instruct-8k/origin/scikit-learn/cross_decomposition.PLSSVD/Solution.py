from sklearn.decomposition import TruncatedSVD

# Initialize TruncatedSVD with n_components=2
svd = TruncatedSVD(n_components=2)

# Fit and transform the data
X_reduced = svd.fit_transform(X)

# Now X_reduced is the reduced dimensionality data
