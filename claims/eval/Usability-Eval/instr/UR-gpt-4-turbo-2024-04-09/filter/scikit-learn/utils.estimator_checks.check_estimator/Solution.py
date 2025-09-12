from sklearn.utils.estimator_checks import check_estimator
from sklearn.linear_model import LinearRegression

# Example estimator
estimator = LinearRegression()
# Checking if the estimator conforms to scikit-learn's conventions
check_estimator(estimator)
