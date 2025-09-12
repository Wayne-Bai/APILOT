import numpy as np
from sklearn.covariance import EllipticEnvelope

# Example data
X = np.array([[1, 2], [2, 3], [1, 3], [2, 2], [5, 7], [8, 8], [6, 7]])

# Define the model with a contamination factor
model = EllipticEnvelope(contamination=0.1)

# Fit the model on the data
model.fit(X)

# Predict the outlier scores (1 for inliers, -1 for outliers)
predictions = model.predict(X)

# Print the outlier scores
print(predictions)
