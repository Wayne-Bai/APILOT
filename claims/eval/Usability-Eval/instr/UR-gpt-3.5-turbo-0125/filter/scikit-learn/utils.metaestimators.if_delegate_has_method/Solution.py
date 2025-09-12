
import functools

def delegate_to_sub_estimator(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        sub_est = getattr(self, 'estimator', None)
        if sub_est is not None:
            return func(sub_est, *args, **kwargs)
        else:
            raise AttributeError("Sub-estimator not found")
    return wrapper

# Example usage:
class MyAlgorithm:
    def __init__(self, estimator):
        self.estimator = estimator
    
    @delegate_to_sub_estimator
    def fit(self, X, y):
        print("Delegated fit method called")
        # Add your custom implementation here

# Create an instance of MyAlgorithm and pass an estimator
# my_algo = MyAlgorithm(estimator)
# my_algo.fit(X_train, y_train)
