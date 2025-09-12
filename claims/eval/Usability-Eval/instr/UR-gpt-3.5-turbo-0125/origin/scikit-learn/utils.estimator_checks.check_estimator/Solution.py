
# Importing scikit-learn library
from sklearn.utils.estimator_checks import _yield_all_checks

# Checking if estimator adheres to scikit-learn conventions
def check_estimator(estimator):
    for check in _yield_all_checks(estimator):
        check(estimator)
