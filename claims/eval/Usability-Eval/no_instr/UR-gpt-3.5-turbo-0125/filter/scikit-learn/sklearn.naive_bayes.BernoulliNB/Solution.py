
import numpy as np

class NaiveBayes:
    def __init__(self):
        self.class_prob = None
        self.feature_probs = None

    def fit(self, X, y):
        self.classes = np.unique(y)
        self.class_prob = {}
        self.feature_probs = {}

        for c in self.classes:
            X_c = X[y == c]
            self.class_prob[c] = len(X_c) / len(X)

            self.feature_probs[c] = np.mean(X_c, axis=0)

    def predict(self, X):
        preds = []
        for x in X:
            pred_probs = {c: np.prod(self.feature_probs[c] ** x * (1 - self.feature_probs[c]) ** (1 - x)) *
                             self.class_prob[c] for c in self.classes}
            preds.append(max(pred_probs, key=pred_probs.get))
        return preds

# Example usage:
X_train = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 1], [0, 1, 1]])
y_train = np.array([0, 1, 0, 1])

model = NaiveBayes()
model.fit(X_train, y_train)

X_test = np.array([[1, 0, 0], [0, 0, 1]])
predictions = model.predict(X_test)
print(predictions)
