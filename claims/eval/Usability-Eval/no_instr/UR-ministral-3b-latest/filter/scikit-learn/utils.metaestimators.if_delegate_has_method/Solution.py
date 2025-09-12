from sklearn.base import BaseEstimator

def delegate_method(sub_estimator):
    def decorator(fn):
        def wrapper(self, *args, **kwargs):
            # Call the sub-estimator
            sub_est_result = getattr(self.sub_estimator_, fn.__name__)(*args, **kwargs)
            # Return the result or modify it as needed
            return sub_est_result
        return wrapper
    return decorator

class DelegateBase(BaseEstimator):
    def __init__(self, sub_estimator, **kwargs):
        self.sub_estimator_ = sub_estimator

    @delegate_method
    def fit(self, X, y, **kwargs):
        return self.sub_estimator_.fit(X, y)

    @delegate_method
    def predict(self, X, **kwargs):
        return self.sub_estimator_.predict(X)

# Example usage
from sklearn.linear_model import LinearRegression

sub_est = LinearRegression()
delegate_base = DelegateBase(sub_estimator=sub_est)
delegate_base.fit([[1, 2], [3, 4]], [5, 6])
predictions = delegate_base.predict([[5, 6]])
print(predictions)
