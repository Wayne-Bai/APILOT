from sklearn.utils import _deprecate_positional_args
from sklearn.utils.metaestimators import available_if
from functools import wraps

def delegated_method(estimator_attr):
    """Decorator for methods that delegate to a sub-estimator.

    Parameters:
    estimator_attr (str): The attribute name of the sub-estimator in the main estimator.

    Usage:
    @delegated_method('sub_estimator')
    def predict(self, X):
        ...
    """
    def check_if_delegate_is_fitted(delegate):
        if not hasattr(delegate, "fit"):
            raise AttributeError(f"The delegated attribute {estimator_attr} should have a 'fit' method.")
        if not hasattr(delegate, 'predict'):
            raise AttributeError(f"The delegated attribute {estimator_attr} should have a 'predict' method.")
            
    @available_if(check_if_delegate_is_fitted)
    def method_decorator(method):
        @wraps(method)
        def _method(self, *args, **kwargs):
            # Get the sub-estimator from the main estimator.
            delegate = getattr(self, estimator_attr)
            # Call the desired method on the sub-estimator.
            meth = getattr(delegate, method.__name__)
            return meth(*args, **kwargs)
        return _method
    return method_decorator
