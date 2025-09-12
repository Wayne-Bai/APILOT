from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

class ComplementNaiveBayes:
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.class_prior = None
        self.feature_prior = None

    def fit(self, X, y):
        n_classes = len(set(y))
        self.class_prior = np.ones(n_classes) / n_classes

        for c in range(n_classes):
            mask = y == c
            self.feature_prior[c] = np.sum(mask) / np.sum(mask * X)

    def predict(self, X):
        pred = np.argmax(self.class_prior * self.feature_prior, axis=1)
        return pred

# Example usage:
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=1000, n_classes=3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = ComplementNaiveBayes(alpha=0.5)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
