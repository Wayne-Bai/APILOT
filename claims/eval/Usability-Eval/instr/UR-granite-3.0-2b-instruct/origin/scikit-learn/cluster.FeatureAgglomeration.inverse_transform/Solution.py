from sklearn.decomposition import TruncatedSVD

# Assuming X is your original data and n_components is the number of components you want to keep
svd = TruncatedSVD(n_components=n_components)
X_new = svd.fit_transform(X)

# If you want to inverse the transformation, you can use the transform method again
X_inverse = svd.transform(X_new)
