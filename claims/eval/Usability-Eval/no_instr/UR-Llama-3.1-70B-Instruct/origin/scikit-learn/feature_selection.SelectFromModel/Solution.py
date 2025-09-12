# Import necessary libraries
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import Pipeline
import numpy as np

# Create a custom meta-transformer class
class ImportanceSelective(BaseEstimator, TransformerMixin):
    def __init__(self, estimator=None):
        self.estimator = estimator if estimator else RandomForestClassifier(n_estimators=100)
        self.support_ = None

    def fit(self, X, y):
        # Create a pipeline with a selector and an estimator
        pipeline = Pipeline([('selector', SelectFromModel(self.estimator)), ('estimator', self.estimator)])
        pipeline.fit(X, y)
        
        # Get the feature support (i.e., the importance weights)
        self.support_ = pipeline.named_steps['selector'].get_support()
        
        return self

    def transform(self, X):
        # Select the features based on the importance weights
        return X[:, self.support_]

    def get_feature_names(self, feature_names):
        # Get the names of the selected features
        return np.array(feature_names)[self.support_]

# Example usage
if __name__ == "__main__":
    # Generate some example data
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=100, n_features=20, random_state=42)

    # Create an instance of the meta-transformer
    transformer = ImportanceSelective()

    # Fit and transform the data
    X_selected = transformer.fit_transform(X, y)

    # Print the shape of the original and transformed data
    print(f"Original shape: {X.shape}, Selected shape: {X_selected.shape}")

    # Get the names of the selected features
    feature_names = [f"Feature {i}" for i in range(X.shape[1])]
    selected_features = transformer.get_feature_names(feature_names)
    print("Selected features:", selected_features)
