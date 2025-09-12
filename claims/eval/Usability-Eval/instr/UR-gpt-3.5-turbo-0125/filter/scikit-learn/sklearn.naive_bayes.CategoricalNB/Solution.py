
import numpy as np

class CategoricalNB:
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        
    def fit(self, X, y):
        self.classes, y_indices = np.unique(y, return_inverse=True)
        self.class_prior_ = np.bincount(y_indices) / len(y)
        
        self.n_class_samples = np.array([np.sum(y == c) for c in self.classes])
        self.n_class_features = np.array([
            np.sum(X[y == c], axis=0) for c in self.classes
        ]) + self.alpha
        
        self.class_log_prior_ = np.log(self.class_prior_)
        self.feature_log_prob_ = np.log(self.n_class_features / np.sum(self.n_class_features, axis=1)[:, None])
        
    def predict(self, X):
        joint_log_likelihood = np.dot(X, self.feature_log_prob_.T) + self.class_log_prior_
        return self.classes[np.argmax(joint_log_likelihood, axis=1)]
