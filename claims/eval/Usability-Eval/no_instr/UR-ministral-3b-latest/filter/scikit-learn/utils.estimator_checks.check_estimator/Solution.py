from sklearn.base import BaseEstimator

def is_estimator_conventional(estimator):
    """Check if an estimator adheres to scikit-learn conventions."""
    if not isinstance(estimator, BaseEstimator):
        print(f"{estimator} is not a scikit-learn BaseEstimator.")
        return False

    # Check if `fit`, `predict`, `predict_proba`, and `score` methods exist
    methods = ["fit", "predict", "predict_proba", "score"]
    for method in methods:
        if not hasattr(estimator, method):
            print(f"{estimator} does not have a {method} method.")
            return False

    # Check if `fit` method takes the expected arguments
    try:
        estimator.fit(np.random.rand(100, 10), np.random.randint(2, size=100))
    except Exception as e:
        print(f"{estimator} does not fit using a random dataset.")
        return False

    # Check if `predict` method takes the expected arguments
    try:
        estimator.predict(np.random.rand(1, 10))
    except Exception as e:
        print(f"{estimator} does not predict using a random dataset.")
        return False

    # Check if `score` method takes the expected arguments
    try:
        estimator.score(X_test, y_test)
    except Exception as e:
        print(f"{estimator} does not score using a test dataset.")
        return False

    print(f"{estimator} adheres to scikit-learn conventions.")
    return True

# Example usage:
from sklearn.ensemble import RandomForestClassifier

estimator = RandomForestClassifier()
is_estimator_conventional(estimator)
