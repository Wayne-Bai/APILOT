from sklearn.preprocessing import StandardScaler

# Assume we have a StandardScaler object and a vector 'X_scaled' of shape (n_samples, n_features)

scaler = StandardScaler()

# For inverse transformation
X_inversed = scaler.inverse_transform(X_scaled)
