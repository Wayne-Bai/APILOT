# Importing necessary libraries
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_is_fitted
from sklearn.utils.estimator_checks import parametrize_with_checks

# Creating a sample estimator class
class MyEstimator(BaseEstimator, ClassifierMixin):
    """A sample estimator that adheres to scikit-learn conventions."""

    def __init__(self, param1=1, param2=2):
        """
        Initialize the estimator.

        Parameters
        ----------
        param1 : int, default=1
            The first parameter.
        param2 : int, default=2
            The second parameter.
        """
        self.param1 = param1
        self.param2 = param2

    def fit(self, X, y):
        """
        Fit the estimator.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input data.
        y : array-like, shape (n_samples,)
            The target values.

        Returns
        -------
        self : object
            The fitted estimator.
        """
        self.X_ = X
        self.y_ = y
        return self

    def predict(self, X):
        """
        Predict the target values.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input data.

        Returns
        -------
        y_pred : array-like, shape (n_samples,)
            The predicted target values.
        """
        check_is_fitted(self)
        y_pred = np.zeros(X.shape[0])
        return y_pred

# Setting up the estimator checks
@parametrize_with_checks([MyEstimator()])
def test_estimators(estimator, check):
    check(estimator)

# Running the estimator checks
test_estimators(MyEstimator(), "fit")
test_estimators(MyEstimator(), "predict")
