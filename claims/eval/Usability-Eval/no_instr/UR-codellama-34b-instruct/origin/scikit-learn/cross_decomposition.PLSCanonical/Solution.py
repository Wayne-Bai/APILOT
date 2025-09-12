import numpy as np
from sklearn.cross_decomposition import PLSRegression, PLSCanonical
from sklearn.preprocessing import StandardScaler

# Generate some sample data
X = np.random.rand(100, 10)
y = np.random.rand(100, 1)

# Scale the data using standard scaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.transform(y)

# Define PLSRegression and PLSCanonical objects
plsreg = PLSRegression(n_components=3, max_iter=1000)
plscan = PLSCanonical(n_components=3, max_iter=1000)

# Perform PLS regression
y_pred = plsreg.fit(X_scaled, y_scaled).predict(X_scaled)

# Perform PLS canonical transformation
X_trans = plscan.fit_transform(X_scaled)

print("PLS Regression Coefficients:")
print(plsreg.coef_)
print("\nPLS Canonical Transformation Matrix:")
print(plscan.components_)
