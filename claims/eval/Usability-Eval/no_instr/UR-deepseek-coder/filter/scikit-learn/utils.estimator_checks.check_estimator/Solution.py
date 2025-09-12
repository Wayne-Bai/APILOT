from sklearn.utils.estimator_checks import check_estimator
from sklearn.linear_model import LogisticRegression

# Example estimator
estimator = LogisticRegression()

# Check if the estimator adheres to scikit-learn conventions
check_estimator(estimator)
