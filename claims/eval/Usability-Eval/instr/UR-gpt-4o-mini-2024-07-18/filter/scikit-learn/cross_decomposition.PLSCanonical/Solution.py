from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
X = np.random.rand(100, 10)  # 100 samples, 10 features
Y = np.random.rand(100, 1)    # 100 target values

# Standardize the data
scaler_X = StandardScaler()
scaler_Y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
Y_scaled = scaler_Y.fit_transform(Y)

# PLS Regression
pls = PLSRegression(n_components=2)  # Specify the number of components
pls.fit(X_scaled, Y_scaled)

# Transform the data
X_transformed = pls.transform(X_scaled)

# Predict using the PLS regressor
Y_pred = pls.predict(X_scaled)

# Inverse transform the predicted values to original scale
Y_pred_original = scaler_Y.inverse_transform(Y_pred)

# Output the transformed data and predictions
print("Transformed X:", X_transformed)
print("Predicted Y (original scale):", Y_pred_original)
