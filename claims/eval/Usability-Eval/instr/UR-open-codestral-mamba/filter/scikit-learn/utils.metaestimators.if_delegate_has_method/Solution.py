import sklearn
from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split
from functools import wraps

class SklearnDelegator(BaseEstimator):
    def __init__(self, sub_estimator):
        self.sub_estimator = sub_estimator

    def fit(self, X, y):
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
        self.sub_estimator.fit(X_train, y_train)
        self.val_score = self.sub_estimator.score(X_val, y_val)
        return self

    def predict(self, X):
        return self.sub_estimator.predict(X)

    def score(self, X, y):
        return self.sub_estimator.score(X, y)

def validate(func):
    @wraps(func)
    def wrapper(self, X, y, *args, **kwargs):
        if not isinstance(self.sub_estimator, BaseEstimator):
            raise ValueError("sub_estimator must be a scikit-learn estimator")
        return func(self, X, y, *args, **kwargs)
    return wrapper

# Now decorate the fit method of SklearnDelegator
SklearnDelegator.fit = validate(SklearnDelegator.fit)
