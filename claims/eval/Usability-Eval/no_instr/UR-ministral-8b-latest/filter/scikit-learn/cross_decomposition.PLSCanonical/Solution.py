import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn_calibration import CalibratedClassifierCV

# Let's assume X_train and y_train are your input data
X_train = np.random.rand(100, 10)
y_train = np.random.rand(100)

# Perform PCA
pca = PCA(n_components=5)
X_train_pca = pca.fit_transform(X_train)

# Use Partial Least Squares transformer (PLST) for feature extraction
class PLST:
    def __init__(self, n_components):
        self.n_components = n_components
        self.pca = PCA(n_components=n_components)

    def fit_transform(self, X):
        return self.pca.fit_transform(X)

plst = PLST(n_components=3)
X_train_transformed = plst.fit_transform(X_train_pca)

# Fit a Linear Regression model
lr = LinearRegression()
lr.fit(X_train_transformed, y_train)

# Output results
print("PLS components:", plst.pca.components_)
print("PLS explained variances:", plst.pca.explained_variance_)
print("Coefficients of Linear Regression:", lr.coef_)
