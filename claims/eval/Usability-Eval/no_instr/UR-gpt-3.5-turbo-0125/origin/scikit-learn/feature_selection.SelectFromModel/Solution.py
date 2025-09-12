
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureSelector(BaseEstimator, TransformerMixin):
    
    def __init__(self, threshold):
        self.threshold = threshold
    
    def fit(self, X, y=None):
        feature_importances = X.mean(axis=0)
        self.selected_features = [index for index, importance in enumerate(feature_importances) if importance > self.threshold]
        return self
    
    def transform(self, X):
        return X[:, self.selected_features]
