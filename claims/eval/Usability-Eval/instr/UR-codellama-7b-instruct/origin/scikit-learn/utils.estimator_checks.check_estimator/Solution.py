
from sklearn.utils.estimator_checks import check_estimator

# define a simple classifier as an example
class MySimpleClassifier:
    def fit(self, X, y):
        pass

    def predict(self, X):
        return np.zeros((X.shape[0], 1))
