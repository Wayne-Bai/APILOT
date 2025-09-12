# Import necessary modules from scikit-learn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
X = np.random.rand(100, 10)  # 100 samples, 10 features
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Perform Partial Least Squares SVD regression
from sklearn.cross_decomposition import PLSRegression
pls_model = PLSRegression(n_components=2)
pls_model.fit(X_train_scaled, y_train)
y_pred = pls_model.predict(X_test_scaled)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean squared error: {mse:.2f}")

# Compare with PCA
pca_model = PCA(n_components=2)
X_train_pca = pca_model.fit_transform(X_train_scaled)
X_test_pca = pca_model.transform(X_test_scaled)
pca_model.fit(X_train_pca, y_train)  # Update y_train with target variable

# Direct PCA with SVD decomposition 
pca_direct = PCA(n_components=2,svd_solver='arpack')  
pca_direct.fit(X_train_scaled)  

y_pred_pca = pca_model.predict(X_test_pca)

# Evaluate the model
mse_pca = mean_squared_error(y_test, y_pred_pca)
print(f"Mean squared error with PCA: {mse_pca:.2f}")

# Compare the accuracy of the two models
if mse < mse_pca:
    print("PLS regression outperforms PCA.")
else:
    print("PCA outperforms PLS regression.")
