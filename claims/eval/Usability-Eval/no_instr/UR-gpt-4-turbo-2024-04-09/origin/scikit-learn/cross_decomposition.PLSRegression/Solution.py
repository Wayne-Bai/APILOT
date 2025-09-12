from sklearn.cross_decomposition import PLSRegression
from sklearn.datasets import make_regression

# Generate some sample data
X, y = make_regression(n_samples=100, n_features=10, n_targets=1, noise=0.1)

# Initialize the PLSRegression model
pls = PLSRegression(n_components=2)

# Fit the model
pls.fit(X, y)

# Predict using the PLS model
predictions = pls.predict(X)

print(predictions)
