# Importing the required Scikit-learn libraries
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Loading the iris dataset
iris = load_iris()
X = iris.data

# Assume you have fitted and transformed your data
scaler = StandardScaler()
X_transformed = scaler.fit_transform(X)

# Now, to reverse or 'inverse' the transformation, you can use the inverse transform method
X_original = scaler.inverse_transform(X_transformed)

# Compare the result
print("Original Data:\n", X[:5])
print("\nTransformed Data:\n", X_transformed[:5])
print("\nInverse Transformed Data (Should be close to original):\n", X_original[:5])
