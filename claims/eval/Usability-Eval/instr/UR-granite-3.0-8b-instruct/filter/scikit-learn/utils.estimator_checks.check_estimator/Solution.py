from sklearn.base import is_estimator

# Assuming estimator is an instance of a class
estimator = ...  # replace with your estimator

# Check if the estimator adheres to scikit-learn conventions
if is_estimator(estimator):
    print("The estimator adheres to scikit-learn conventions.")
else:
    print("The estimator does not adhere to scikit-learn conventions.")
