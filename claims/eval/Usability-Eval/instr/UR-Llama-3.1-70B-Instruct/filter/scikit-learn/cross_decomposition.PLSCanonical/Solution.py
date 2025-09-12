# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import NMF
from sklearn.cross_decomposition import PLSRegression as PLSR
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Create a sample dataset (in real use, you should import your dataset)
np.random.seed(0)
X = np.random.rand(100, 10)
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Apply non-negative matrix factorization (NMF) for feature selection/extraction
nmf = NMF(n_components=2, init='random', random_state=0)
X_train_nmf = nmf.fit_transform(X_train_scaled)
X_test_nmf = nmf.transform(X_test_scaled)

# Create a Partial Least Squares (PLS) regressor
pls = PLSR(n_components=2)

# Train the PLS regressor
pls.fit(X_train_nmf, y_train)

# Make predictions
y_pred = pls.predict(X_test_nmf)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Partial Least Squares Regressor Performance:')
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')
