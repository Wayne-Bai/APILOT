from sklearn.decomposition import PCA
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.transformers import FunctionTransformer
import numpy as np

# Sample data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])  # Features
y = np.array([1, 3, 5, 7])  # Target variable

# Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Scaler and StandardScaler combining
    ('pca', FunctionTransformer(PCA(n_components=1).fit_transform)),
    ('lasso', Lasso(alpha=1.0))  # Lasso regressor
])

# Fit and predict
pipeline.fit(X, y)
y_pred = pipeline.predict(X)

print(f"Predictions: {y_pred}")
