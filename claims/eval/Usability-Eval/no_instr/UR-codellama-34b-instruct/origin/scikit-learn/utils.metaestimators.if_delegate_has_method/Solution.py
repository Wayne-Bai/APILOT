from sklearn.base import BaseEstimator, clone

class DelegatingEstimator(BaseEstimator):
    def __init__(self, sub_estimator):
        self.sub_estimator = sub_estimator
    
    def fit(self, X, y=None):
        # Clone the sub-estimator so we can make sure it's trained on the same data
        cloned_sub_estimator = clone(self.sub_estimator)
        
        # Fit the sub-estimator on the data
        cloned_sub_estimator.fit(X, y)
        
        # Return self so we can chain the fit method
        return self
    
    def predict(self, X):
        # Predict using the sub-estimator's predict method
        return self.sub_estimator.predict(X)
