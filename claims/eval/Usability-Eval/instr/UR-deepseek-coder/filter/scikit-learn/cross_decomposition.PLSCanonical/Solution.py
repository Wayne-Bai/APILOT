import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Example data
X = np.array([[0.0, 0.0, 1.0],
              [1.0, 0.0, 0.0],
              [2.0, 2.0, 2.0],
              [2.0, 5.0, 4.0]])
y = np.array([[0.1, -0.2],
              [0.9, 1.1],
              [6.2, 5.9],
              [11.9, 12.3]])

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y)

# Create a PLS regression model
pls = PLSRegression(n_components=2)

# Fit the model
pls.fit(X_scaled, y_scaled)

# Predict
y_pred = pls.predict(X_scaled)

# Inverse transform to get the original scale predictions
y_pred_original_scale = scaler.inverse_transform(y_pred)

print("Predicted y:", y_pred_original_scale)
