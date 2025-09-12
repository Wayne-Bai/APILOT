# Importing the necessary libraries
from sklearn.cross_decomposition import PLSCanonical, PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import numpy as np

# Generating random data for demonstration purposes
np.random.seed(0)
X = np.random.rand(100, 3)  # features
y = 2 * X[:, 0] + 3 * X[:, 1] + 4 * X[:, 2] + np.random.randn(100)  # target variable

# Preprocess the data
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=0.2, random_state=42)

# Partial Least Squares (PLS) Regression
pls = PLSRegression(n_components=2)
pls.fit(X_train, y_train)
y_pred = pls.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse}')

# Partial Least Squares (PLS) transformer
pls_transformer = PLSCanonical(n_components=2)
X_std_parked = pls_transformer.fit_transform(X_train, y_train)
X_test_parked = pls_transformer.transform(X_test)

# Print the shape of the transformed data
print(f'Original shape of X_std_parked: {X_train.shape}, Transformed shape of X_std_parked: {X_std_parked.shape}')
print(f'Original shape of X_test_parked: {X_test.shape}, Transformed shape of X_test_parked: {X_test_parked.shape}')
