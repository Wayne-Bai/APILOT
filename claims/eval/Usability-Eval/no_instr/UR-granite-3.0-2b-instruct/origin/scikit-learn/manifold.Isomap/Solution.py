from sklearn.manifold import Isomap

# Assuming X is your data
isaomap = Isomap(n_components=2, random_state=42)
X_2d = isaomap.fit_transform(X)
