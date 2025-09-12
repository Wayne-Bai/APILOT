from sklearn.utils.validation import check_is_fitted, check_array
from sklearn.base import is_classifier, is_regressor

def check_estimator(estimator, X, y):
    # Check if the estimator adheres to scikit-learn conventions
    if not (is_classifier(estimator) or is_regressor(estimator)):
        raise ValueError("The passed estimator is neither a classifier nor a regressor.")

    # Fit the estimator
    estimator.fit(X, y)

    # Check if the estimator is fitted
    check_is_fitted(estimator)

    # Check that input is an appropriate array
    X_checked = check_array(X)
    
    return X_checked
