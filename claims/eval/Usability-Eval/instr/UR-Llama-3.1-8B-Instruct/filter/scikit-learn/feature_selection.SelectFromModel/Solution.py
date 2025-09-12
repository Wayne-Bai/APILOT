# Import necessary modules from scikit-learn
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
import pandas as pd
import numpy as np

# Create a sample dataset
diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

# Define the feature selector class
class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, threshold=0.1):
        self.threshold = threshold
        self.features = None
    
    def fit(self, X, y=None):
        self.feature_importances_ = self.model.feature_importances_
        # We're using a Random Forest Regressor here, which assigns importance values to features
        return self

    def transform(self, X):
        if self.feature_importances_ is not None:
            mask = self.feature_importances_ > self.threshold
            self.features = X.columns[mask]
            return X[self.features]
        return None

    def fit_transform(self, X, y=None, **fit_params):
        self.fit(X, y)
        return self.transform(X)

# Create a FeatureSelector object
fs = FeatureSelector()

# Create an ExtraTreesRegressor feature selector 
etr = ExtraTreesRegressor(n_estimators=10, n_jobs=-1)
etr_fs = ExtraTreesRegressor(feature_importances_=True, n_estimators=10, n_jobs=-1)

# Use Pipeline to pipeline=train => feature selector ascertain important features
pipeline = Pipeline([
    ('etr_fs', etr_fs),
    ('select_features', fs)
])
pipeline.fit(df.drop('target', axis=1), df['target']) 
feat_names = df.drop('target', axis=1).columns[pipeline.named_steps['select_features'].features]

print("Feature importances:", pipeline.named_steps['etr_fs'].feature_importances_)
print("Features selected:", feat_names)
