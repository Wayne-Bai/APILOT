from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import check_classification_targets

class MyEstimator(BaseEstimator, ClassifierMixin):
    def __init__(self):
        self.n_classes_ = 0

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.n_classes_ = len(np.unique(y))
        check_classification_targets(y, allow_none='auto')
        self.coef_ = np.random.rand(X.shape[1], self.n_classes_)
        self.intercept_ = np.random.rand(self.n_classes_)
        return self

    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X)
        return np.argmax(np.dot(X, self.coef_) + self.intercept_, axis=1)

    def score(self, X, y):
        X, y = check_X_y(X, y)
        y_pred = self.predict(X)
        return np.mean(y == y_pred)
