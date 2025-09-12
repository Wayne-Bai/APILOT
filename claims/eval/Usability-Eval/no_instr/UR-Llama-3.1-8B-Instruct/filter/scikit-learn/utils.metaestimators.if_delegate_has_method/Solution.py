# Importing necessary libraries
from sklearn.base import BaseEstimator, make_pipeline
from functools import wraps

# Defining a decorator to check if a method is delegated
def is_delegate(method):
    if not callable(method):
        return False
    if hasattr(method, '__self__') and isinstance(method.__self__, BaseEstimator):
        return True
    return False

# Defining a decorator to check if a method is delegated to a sub-estimator
def delegated_attribute(func):
    """
    Checks if the method decorated is delegated to a sub-estimator.
    
    Parameters:
    ----------
    func : method
        The method to be decorated.
        
    Returns:
    -------
    result : bool
        True if the method is delegated to a sub-estimator, False otherwise.
    """
    return False if is_delegate(func) else True

# Defining a class to test the decorator
class TestClass(BaseEstimator):
    def __init__(self):
        self.dtype_list = make_pipeline(BaseEstimator(), BaseEstimator(name='step1'))
        
    def method_delegated(self):
        # This method is delegated to a sub-estimator in'self.dtype_list'
        __fit__ = self.dtype_list.steps[-1][1].fit
        __fit__.__wrapped__.__defaults__ = (None, None, None, None)
        __fit__(self.dtype_list.steps[-1][1], None)
        
    def method_not_delegated(self):
        # This method is not delegated to a sub-estimator
        pass
        
    def test(self):
        print("TestClass test method started.")
        
# Creating an instance of TestClass
test_instance = TestClass()
        
# Decorating test_instance's methods and checking if they are delegated
print(hasattr(test_instance.method_delegated, '__wrapped__'))  # This should be True
print(hasattr(test_instance.method_not_delegated, '__wrapped__'))  # This should be False
