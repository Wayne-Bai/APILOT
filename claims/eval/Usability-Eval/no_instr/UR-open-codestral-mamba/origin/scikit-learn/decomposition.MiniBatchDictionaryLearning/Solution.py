# Importing Required Modules from scikit-learn
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.decomposition import SparseCoder
import numpy as np

class MiniBatchDictLearning(BaseEstimator, TransformerMixin):
    def __init__(self, batch_size=256, n_iter=100):
        self.batch_size = batch_size
        self.n_iter = n_iter
        self.coder = SparseCoder(dictionary=None, transform_n_nonzero_coefs=None,
                                 transform_alpha=1.0, transform_algorithm='lasso_lars',
                                 positive_code=False, transform_epsilon=1e-10)

    def fit(self, X, y=None):
        n_samples, n_features = X.shape
        n_batches = n_samples // self.batch_size

        for _ in range(self.n_iter):
            np.random.shuffle(X)
            for i in range(n_batches):
                batch = X[i * self.batch_size:(i + 1) * self.batch_size]
                self.coder.transform(batch)

    def transform(self, X):
        return self.coder.transform(X)

# create dictionary for testing
D = np.array([[1, 1], [2, 1], [1, 2]])
X = np.array([[1, 2], [3, 4]])

# Initialize the MiniBatchDictLearning class
mini_batch_dict_learning = MiniBatchDictLearning(batch_size=1, n_iter=2)

# Fit the model to the data
mini_batch_dict_learning.fit(D)

# Transform the data
X_transformed = mini_batch_dict_learning.transform(X)
print(X_transformed)
