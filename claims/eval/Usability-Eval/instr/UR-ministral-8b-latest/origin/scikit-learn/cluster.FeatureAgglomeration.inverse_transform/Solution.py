import numpy as np
from sklearn.preprocessing import StandardScaler

# Create a vector of size n_features
n_features = 10
data = np.random.rand(n_features)

# Standard Scaling
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data.reshape(-1, 1))
print(data_scaled)

# Inverse the transformation
data_inverse = scaler.inverse_transform(data_scaled)
print(np.round(data_inverse, 2))
