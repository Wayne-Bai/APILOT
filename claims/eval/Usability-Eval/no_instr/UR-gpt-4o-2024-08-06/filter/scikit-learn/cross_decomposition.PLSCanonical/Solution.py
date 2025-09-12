from sklearn.cross_decomposition import PLSRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Generate some example data
X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize PLSRegressor with desired number of components
pls = PLSRegression(n_components=2)

# Fit the model
pls.fit(X_train_scaled, y_train)

# Transform data
X_train_pls = pls.transform(X_train_scaled)
X_test_pls = pls.transform(X_test_scaled)

# Make predictions
y_pred = pls.predict(X_test_scaled)

# Calculate mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Display transformed data for first 5 samples (as an example)
print("Transformed Training Data (first 5 samples):")
print(X_train_pls[:5])
