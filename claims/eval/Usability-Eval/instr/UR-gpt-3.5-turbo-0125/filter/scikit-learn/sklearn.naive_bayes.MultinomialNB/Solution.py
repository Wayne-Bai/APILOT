
import numpy as np

class MultinomialNB:
    def __init__(self, alpha=1.0):
        self.alpha = alpha

    def fit(self, X, y):
        n_classes = np.max(y) + 1
        n_features = X.shape[1]
        self.class_log_prior_ = np.log(np.bincount(y) / len(y))
        self.feature_log_prob_ = np.empty(shape=(n_classes, n_features))

        for i in range(n_classes):
            class_idx = np.where(y == i)
            class_features = X[class_idx]
            smoothed_class_features = class_features + self.alpha
            self.feature_log_prob_[i] = np.log(smoothed_class_features.sum(axis=0) / smoothed_class_features.sum())

    def predict_log_proba(self, X):
        return X.dot(self.feature_log_prob_.T) + self.class_log_prior_

    def predict(self, X):
        return np.argmax(self.predict_log_proba(X), axis=1)
