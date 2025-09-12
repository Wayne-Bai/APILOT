import functools
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted

def delegate(method_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, 'estimator'):
                raise ValueError("Sub-estimator is not defined.")
            if not hasattr(self.estimator, method_name):
                raise ValueError(f"Sub-estimator does not have method '{method_name}'.")
            return getattr(self.estimator, method_name)(*args, **kwargs)
        return wrapper
    return decorator

class DelegateEstimator(BaseEstimator, TransformerMixin):
    def __init__(self, estimator):
        self.estimator = estimator
    
    @delegate('fit')
    def fit(self, X, y=None):
        pass
    
    @delegate('transform')
    def transform(self, X):
        pass
    
    @delegate('fit_transform')
    def fit_transform(self, X, y=None):
        pass
    
    @delegate('get_params')
    def get_params(self, deep=True):
        pass
    
    @delegate('set_params')
    def set_params(self, **params):
        pass
    
    def check_is_fitted(self):
        check_is_fitted(self.estimator)

from sklearn.linear_model import LogisticRegression
estimator = LogisticRegression()
delegate_estimator = DelegateEstimator(estimator)

# Usage
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

delegate_estimator.fit(X_train, y_train)
y_pred = delegate_estimator.estimator.predict(X_test)
