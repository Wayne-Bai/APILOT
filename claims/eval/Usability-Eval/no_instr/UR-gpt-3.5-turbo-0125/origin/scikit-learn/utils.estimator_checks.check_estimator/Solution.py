
import sklearn

def check_estimator_conventions(estimator):
    try:
        _ = estimator.fit
        _ = estimator.predict
        _ = estimator.score
    except AttributeError:
        raise AttributeError("Estimator does not adhere to scikit-learn conventions")
    print("Estimator adheres to scikit-learn conventions")

# Example usage:
# check_estimator_conventions(YourEstimator())
