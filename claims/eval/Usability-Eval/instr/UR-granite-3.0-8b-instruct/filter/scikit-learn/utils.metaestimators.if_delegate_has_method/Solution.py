from sklearn.base import BaseEstimator

def delegate_to_subestimator(subestimator):
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            return subestimator.method(self, *args, **kwargs)
        return wrapper
    return decorator

class MyEstimator(BaseEstimator):
    def __init__(self, subestimator):
        self.subestimator = subestimator

    @delegate_to_subestimator
    def my_method(self, *args, **kwargs):
        pass
