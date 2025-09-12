from sklearn.cross_decomposition import PLSRegression
from sklearn.decomposition import PLSTransformer
from sklearn.preprocessing import StandardScaler

# Example data
import numpy as np
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
y = np.array([1, 2, 3, 4])

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply the PLS Transformer
pls_transformer = PLSTransformer(n_components=2)
X_transformed = pls_transformer.fit_transform(X_scaled)

# Fit the PLS Regression model
pls_regressor = PLSRegression(n_components=2)
pls_regressor.fit(X_transformed, y)

# Make predictions
X_transformed_new = pls_transformer.transform(scaler.transform(np.array([[13, 14, 15]])))
predicted_val = pls_regressor.predict(X_transformed_new)

print(predicted_val)
