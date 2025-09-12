from sklearn.covariance import LedoitWolf
from sklearn.model_selection import cross_val_score
from sklearn.base import BaseEstimator

# Define a custom estimator that uses cross-validated LedoitWolf to select the l1 penalty
class SparseInverseCovariance(BaseEstimator):
    def __init__(self):
        self._estimator = LedoitWolf()

    def fit(self, X, y=None):
        lmax = [0.5*np.log(score(X))/np.iinfo(np.intc).max() for score in range(10, 100)]
        cv_results = []
        for l in lmax:
            self._estimator.lambda_ = l
            scores = cross_val_score(self._estimator, X, y, cv=3)
            cv_results.append(scores.mean())

        best_lambda = lmax[np.argmax(cv_results)]
        self._estimator.lambda_ = best_lambda
        return self._estimator.fit(X)

    def score(self, X, y=None):
        return self._estimator.score(X, y)
