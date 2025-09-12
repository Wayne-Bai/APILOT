from sklearn.base import BaseEstimator
from functools import wraps

def delegate_to_subestimator(subestimator):
    def decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            return subestimator.method(self, *args, **kwargs)
        return wrapper
    return decorator

class MyEstimator(BaseEstimator):
    def __init__(self, subestimator):
        self.subestimator = subestimator

    @delegate_to_subestimator('subestimator')
    def my_method(self, arg1, arg2):
        pass
