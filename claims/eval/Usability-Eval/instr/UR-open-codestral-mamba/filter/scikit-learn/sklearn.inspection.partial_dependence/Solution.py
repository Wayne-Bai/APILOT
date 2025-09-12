from sklearn.inspection import PartialDependenceDisplay
from sklearn.datasets import make_friedman1
from sklearn.ensemble import GradientBoostingRegressor

# load dataset
X, y = make_friedman1()

# train a gradient boosting regressor
reg = GradientBoostingRegressor(n_estimators=50, learning_rate=0.1, max_depth=3)
reg.fit(X, y)

# plot partial dependence of first feature
disp = PartialDependenceDisplay.from_estimator(reg, X, [0])
disp.figure_
