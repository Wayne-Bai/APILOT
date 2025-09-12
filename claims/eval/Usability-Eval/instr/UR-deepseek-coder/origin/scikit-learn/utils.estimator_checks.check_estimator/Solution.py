from sklearn.utils.estimator_checks import check_estimator
from sklearn.linear_model import LogisticRegression

# Define a custom estimator that adheres to scikit-learn conventions
class CustomEstimator(LogisticRegression):
    pass

# Check if the custom estimator adheres to scikit-learn conventions
check_estimator(CustomEstimator)
