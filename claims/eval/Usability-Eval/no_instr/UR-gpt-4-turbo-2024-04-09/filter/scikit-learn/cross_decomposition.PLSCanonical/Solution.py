import numpy as np
from sklearn.cross_decomposition import PLSSVD, PLSRegression
from sklearn.model_selection import train_test_split

# Generating some random data
np.random.seed(0)
n_samples = 100
n_features = 10

X = np.random.normal(size=(n_samples, n_features))
y = X[:, 0] + 2 * X[:, 1] + np.random.normal(size=n_samples)

# Splitting the data into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Applying Partial Least Squares Singular Value Decomposition (PLSSVD)
pls_svd = PLSSVD(n_components=2)
pls_svd.fit(X_train, y_train)
X_train_transformed = pls_svd.transform(X_train)

# Fitting the Partial Least Squares Regression (PLSRegression)
pls_regression = PLSRegression(n_components=2)
pls_regression.fit(X_train, y_train)

# Making predictions
y_pred = pls_regression.predict(X_test)

# Evaluating the performance (e.g., using R2 score)
from sklearn.metrics import r2_score
r2_score = r2_score(y_test, y_pred)

print(f'R2 score: {r2_score:.3f}')

# If you need to visualize the transformed features
import matplotlib.pyplot as plt
plt.scatter(X_train_transformed[:, 0], X_train_transformed[:, 1], c=y_train, cmap='viridis')
plt.xlabel('PLS Component 1')
plt.ylabel('PLS Component 2')
plt.colorbar(label='Target variable')
plt.title('PLS-SVD Transform')
plt.show()
