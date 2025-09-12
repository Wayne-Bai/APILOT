from sklearn.preprocessing import StandardScaler
import numpy as np

# Assuming X is your input data
scaler = StandardScaler()
scaler.fit(X)

# Inverse transform
X_inverse = scaler.inverse_transform(X)

# Return vector of size n_features
X_inverse = np.atleast_2d(X_inverse)
