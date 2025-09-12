# Importing the scikit-learn
from sklearn.covariance import GraphLasso

# Create a sparse inverse covariance estimation model with l1-penalized estimator
model = GraphLasso(alpha=0.1)
