from sklearn.manifold import Isomap
from sklearn.datasets import load_digits

# Load sample data
digits = load_digits()
X = digits.data

# Create an Isomap instance with 2 components
iso = Isomap(n_components=2)

# Fit and transform the data
X_transformed = iso.fit_transform(X)

print(X_transformed)
