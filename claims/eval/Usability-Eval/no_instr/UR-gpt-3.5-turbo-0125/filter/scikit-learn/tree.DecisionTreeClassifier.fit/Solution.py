
import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTreeClassifier:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.n_classes = len(np.unique(y))
        self.root = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        n_samples, n_features = X.shape
        n = len(np.unique(y))

        if (n == 1) or (depth == self.max_depth):
            leaf_value = np.argmax(np.bincount(y))
            return Node(value=leaf_value)

        feature_idxs = np.random.choice(n_features, 2, replace=False)
        best_feature_idx, best_threshold = self._best_criteria(X, y, feature_idxs)

        left_idxs = X[:, best_feature_idx] < best_threshold
        right_idxs = X[:, best_feature_idx] >= best_threshold

        left = self._build_tree(X[left_idxs], y[left_idxs], depth + 1)
        right = self._build_tree(X[right_idxs], y[right_idxs], depth + 1)

        return Node(best_feature_idx, best_threshold, left, right)

    def _best_criteria(self, X, y, feature_idxs):
        best_gini = 1
        for feature_idx in feature_idxs:
            thresholds = np.unique(X[:, feature_idx])
            for threshold in thresholds:
                gini = self._gini_impurity(X, y, feature_idx, threshold)
                if gini < best_gini:
                    best_gini = gini
                    best_criteria = (feature_idx, threshold)
        return best_criteria

    def _gini_impurity(self, X, y, feature_idx, threshold):
        left_idxs = X[:, feature_idx] < threshold
        right_idxs = X[:, feature_idx] >= threshold

        left_gini = np.sum([count / len(y[left_idxs]) * (1 - np.sum(np.square(Counter(y[left_idxs]).values()) / len(y[left_idxs])**2)) for count in Counter(y[left_idxs]).values()])
        right_gini = np.sum([count / len(y[right_idxs]) * (1 - np.sum(np.square(Counter(y[right_idxs]).values()) / len(y[right_idxs])**2)) for count in Counter(y[right_idxs]).values()])

        gini_impurity = (len(y[left_idxs])/len(y)) * left_gini + (len(y[right_idxs])/len(y)) * right_gini

        return gini_impurity
