from sklearn.base import BaseEstimator, Regressor

class SimpleRegressor(BaseEstimator, Regressor):
    def __init__(self, constant=0.0):
        self.constant = constant

    def fit(self, X, y):
        self.header = X.columns
        self.coef_ = 0.5 * np.ones(len(self.header))
        self.intercept_ = self.constant
        return self

    def predict(self, X):
        if not self.header in X.columns:
            raise ValueError("All features to be predicted must be in the input data.")
        return self.intercept_ + np.dot(X[self.header], self.coef_)
