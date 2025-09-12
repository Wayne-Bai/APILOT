
from sklearn.utils.estimator_checks import check_estimator

def check_if_estimator(estimator):
    """
    Check if an estimator adheres to scikit-learn conventions.
    Parameters:
    estimator: object
        The estimator to check.
    """
    try:
        check_estimator(estimator)
        print("The estimator is compliant with scikit-learn conventions.")
    except Exception as e:
        print("The estimator is not compliant with scikit-learn conventions:", str(e))
