from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Load dataset
X = ... # Feature matrix
y = ... # Target vector

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit L1-penalized linear regression model
model = LinearRegression(alpha=0.5, fit_intercept=True, normalize=False)
model.fit(X_scaled, y)

# Predict on test set
X_test = ... # Test feature matrix
y_pred = model.predict(X_test)

# Evaluate performance
mse = mean_squared_error(y_true=y, y_pred=y_pred)
print(f"MSE: {mse}")
