from sklearn.manifold import Isomap

# Assuming 'X' is your data
# X = ...

isomap = Isomap(n_components=2)
X_embedded = isomap.fit_transform(X)
