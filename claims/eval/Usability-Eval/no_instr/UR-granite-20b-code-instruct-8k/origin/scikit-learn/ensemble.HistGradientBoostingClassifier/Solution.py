from sklearn.experimental import enable_hist_gradient_boosting  # noqa
from sklearn.ensemble import HistGradientBoostingClassifier

# X should be a 2-dimensional array with shape=(n_samples, n_features)
# y should be a 1-dimensional array with shape=(n_samples,)
# The input samples.
X = ...

# The target values (class labels) as integers or strings.
y = ...

# Initialize the model
clf = HistGradientBoostingClassifier()

# Fit the model to the data
clf.fit(X, y)
