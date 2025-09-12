from sklearn.covariance import EllipticEnvelope

# Example data
X = [[-1.1, -1.5], [0, 0], [1.1, 1.1], [9, 8], [10, 10]]  # Example dataset

# Create an EllipticEnvelope model
model = EllipticEnvelope(support_fraction=1., contamination=0.1)

# Fit the model to the data
model.fit(X)

# Detect the outliers
print("Outlier detection (1 for inliers, -1 for outliers):")
print(model.predict(X))
