from sklearn import base

def check_estimator(estimator):
    """
    Check if estimator adheres to scikit-learn conventions.
    """
    # Check if it has fit method
    if not hasattr(estimator, 'fit'):
        return False
    # Check if it has predict or predict_proba method
    if not hasattr(estimator, 'predict') and not hasattr(estimator, 'predict_proba'):
        return False
    # Check if it inherits from BaseEstimator
    if not isinstance(estimator, base.BaseEstimator):
        return False
    return True
