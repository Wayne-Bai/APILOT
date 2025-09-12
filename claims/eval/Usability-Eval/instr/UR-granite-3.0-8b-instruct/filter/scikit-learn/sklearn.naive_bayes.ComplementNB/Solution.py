import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score

class ComplementNaiveBayes:
    def __init__(self, alpha=1.0):
        self.alpha = alpha

    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.n_classes_ = len(self.classes_)

        self.class_priors_ = np.zeros(self.n_classes_)
        self.class_priors_ += self.alpha / self.n_classes_

        self.feature_log_prob_ = {}
        for c in self.classes_:
            self.feature_log_prob_[c] = np.zeros(X.shape[1])

        for c in self.classes_:
            X_c = X[y == c]
            self.class_priors_[c] = np.sum(X_c.shape[0] / X.shape[0])
            for i in range(X.shape[1]):
                self.feature_log_prob_[c][i] = np.log(np.sum(X_c[:, i]) + self.alpha)

    def predict(self, X):
        y_pred = np.zeros(X.shape[0])
        for i in range(X.shape[0]):
            max_prob = -np.inf
            max_class = None
            for c in self.classes_:
                prob = self.class_priors_[c]
                for j in range(X.shape[1]):
                    prob += self.feature_log_prob_[c][j] * X[i, j]
                if prob > max_prob:
                    max_prob = prob
                    max_class = c
            y_pred[i] = max_class
        return y_pred
