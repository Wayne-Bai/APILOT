
import types

def delegate_to_subestimator(func):
    def func_wrapper(self, *args, **kwargs):
        return func(self.__dict__['estimator'], *args, **kwargs)
        
    return func_wrapper

class Delegator:
    def __init__(self, estimator):
        self.estimator = estimator
        
    @delegate_to_subestimator
    def fit(self, X, y=None):
        pass
    
    @delegate_to_subestimator
    def predict(self, X):
        pass

# Example Usage
from sklearn.linear_model import LinearRegression

estimator = LinearRegression()
delegator = Delegator(estimator)

X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

delegator.fit(X, y)
predictions = delegator.predict(X)
