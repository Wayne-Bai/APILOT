from sklearn.preprocessing import StandardScaler
import numpy as np

# Generate some sample data
X_transformed = np.random.rand(5, 2)

# Initialize a StandardScaler instance
scaler = StandardScaler()

# Fit the scaler on the data (this computes the mean and std. dev)
scaler.fit(X_transformed)

# Transform the data
X_transformed = scaler.transform(X_transformed)

# Now, inverse the transformation
X_inverse_transformed = scaler.inverse_transform(X_transformed)

print(X_inverse_transformed)
