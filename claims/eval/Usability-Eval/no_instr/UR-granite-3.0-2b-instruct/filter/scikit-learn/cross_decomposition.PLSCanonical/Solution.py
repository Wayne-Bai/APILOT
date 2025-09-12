from sklearn.decomposition import PartialLeastSquares
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_boston
import numpy as np

# Load the Boston housing dataset
boston = load_boston()
X, y = boston.data, boston.target

# Create a Partial Least Squares transformer
pls = PartialLeastSquares(n_components=5)

# Create a Linear Regression regressor
lr = LinearRegression()

# Create a pipeline that first applies the PLS transformer and then the regressor
pipeline = Pipeline([
    ('pls', pls),
    ('lr', lr)
])

# Fit the pipeline to the data
pipeline.fit(X, y)

# Print the coefficients of the regressor
print(pipeline.named_steps['lr'].coef_)
