from sklearn.preprocessing import StandardScaler
import numpy as np

# Assume X_train is your training data and scaler is your trained scaler
scaler = StandardScaler()
scaler.fit(X_train)

# Assume X_test is your test data
X_test_scaled = scaler.transform(X_test)

# To invert the transformation and return a vector of size n_features, you can use the inverse_transform method
X_test_inverted = scaler.inverse_transform(X_test_scaled)

# Print the inverted vector
print(X_test_inverted)
