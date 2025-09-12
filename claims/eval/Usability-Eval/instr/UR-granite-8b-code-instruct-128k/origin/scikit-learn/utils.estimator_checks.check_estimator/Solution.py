
from sklearn.utils.estimator_checks import check_estimator

# Import your estimator here
from your_package.your_estimator import YourEstimator

def test_your_estimator():
    # Check if your estimator adheres to scikit-learn conventions
    check_estimator(YourEstimator)
