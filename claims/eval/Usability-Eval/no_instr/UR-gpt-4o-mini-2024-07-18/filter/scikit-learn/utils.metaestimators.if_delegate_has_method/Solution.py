from sklearn.base import BaseEstimator, clone

def delegate_property(attr_name):
    """Decorator to delegate method calls to a sub-estimator."""
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # Get the sub-estimator using self.sub_estimator
            sub_estimator = self.sub_estimator

            # Ensure the sub-estimator is properly cloned for thread-safety
            sub_estimator_cloned = clone(sub_estimator)

            # Call the function on the sub-estimator
            if hasattr(sub_estimator_cloned, attr_name):
                method = getattr(sub_estimator_cloned, attr_name)
                return method(*args, **kwargs)

            raise NotImplementedError(f"{attr_name} not implemented in sub-estimator.")
        
        return wrapper
    return decorator

# Example usage in a custom estimator class
class CustomEstimator(BaseEstimator):
    def __init__(self, sub_estimator):
        self.sub_estimator = sub_estimator

    @delegate_property('fit')
    def fit(self, X, y):
        pass  # The actual fit logic can go here

    @delegate_property('predict')
    def predict(self, X):
        pass  # The actual predict logic can go here
