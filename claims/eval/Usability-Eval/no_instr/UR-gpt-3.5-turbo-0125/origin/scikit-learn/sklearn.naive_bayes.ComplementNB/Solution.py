from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np

class ComplementNB(BaseEstimator, ClassifierMixin):
    
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        
    def fit(self, X, y):
        n_classes = np.unique(y)
        n_features = X.shape[1]
        self.class_prior_ = np.bincount(y) / len(y)
        self.feature_log_prob_ = np.zeros((len(n_classes), n_features))
        
        for i in n_classes:
            Xi = X[y == i]
            self.feature_log_prob_[i] = np.log((Xi.sum(axis=0) + self.alpha) / (Xi.sum() + self.alpha * n_features))
        
        return self
    
    def predict_log_proba(self, X):
        return [(self.feature_log_prob_ * x).sum(axis=1) for x in X]
    
    def predict(self, X):
        return np.argmax(self.predict_log_proba(X), axis=1)
