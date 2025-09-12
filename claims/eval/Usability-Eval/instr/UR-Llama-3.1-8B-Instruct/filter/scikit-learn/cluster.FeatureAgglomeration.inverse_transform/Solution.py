# Import necessary modules
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils import check_array
from sklearn.utils._testing import assert_array_equal
import numpy as np

# Define a custom transformer to perform inverse scaling
class ScalingInverter(BaseEstimator, TransformerMixin):
    def __init__(self, scaler):
        self.scaler = scaler
        self.scale_ = None
        self._fit_called = False

    def fit(self, X, y=None):
        self.scale_ = self.scaler.scale_
        self._fit_called = True
        return self

    def transform(self, X):
        # Check if the fit method has been called
        assert (self._fit_called), "The ScalingInverter has not been fitted yet."

        # Calculate the inverse scaled values
        scaled_values = self.scaler.transform(X)
        return scaled_values / self.scale_

# Define a function to invert the transformation and return a vector of size n_features
def invert_scaling(X, scaler):
    transformer = ScalingInverter(scaler)
    return transformer.fit_transform(X)

# Create a sample dataset
n_samples = 100
n_features = 5
X = np.random.rand(n_samples, n_features)

# Define the preprocessing pipeline
scaler = StandardScaler()
preprocessing_pipeline = Pipeline([
    ('scaler', scaler)
])

# Fit the pipeline and transform the data
X_scaled = preprocessing_pipeline.fit_transform(X)

# Invert the scaling
X_inverted = invert_scaling(X_scaled, preprocessing_pipeline['scaler'])

assert_array_equal(X, X_inverted * preprocessing_pipeline['scaler'].scale_)
