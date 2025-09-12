
from sklearn.preprocessing import StandardScaler

# Create a scaler object and fit it to the data
scaler = StandardScaler()
scaler.fit(X)

# Apply the inverse transformation to the data
X_inv = scaler.inverse_transform(X)
