
import numpy as np

class DictionaryLearning:
    def __init__(self, n_components=2, alpha=1, max_iter=100):
        self.n_components = n_components
        self.alpha = alpha
        self.max_iter = max_iter

    def fit_transform(self, X):
        D = np.random.rand(X.shape[0], self.n_components)
        for _ in range(self.max_iter):
            for i in range(X.shape[1]):
                D += self.alpha * np.outer(X[:, i] - np.dot(D, np.dot(D.T, X[:, i])), np.dot(D.T, X[:, i]))
        return D

# Example usage
X = np.array([[1, 2, 3], [4, 5, 6]])
dl = DictionaryLearning(n_components=2)
D = dl.fit_transform(X)
print(D)
