from sklearn.preprocessing import normalize
from sklearn.linear_model import Ridge
import numpy as np

# Example data
X = np.array([[1, 2], [3, 4], [5, 6]])

# Normalize the data
X_normalized = normalize(X, axis=0)

# Train a linear model
model = Ridge(alpha=1.0)
model.fit(X_normalized, X_normalized)

# Assume the model is trained and the inverse transformation is required
inverse_transformed = model.inverse_transform(X_normalized)

print(inverse_transformed)
