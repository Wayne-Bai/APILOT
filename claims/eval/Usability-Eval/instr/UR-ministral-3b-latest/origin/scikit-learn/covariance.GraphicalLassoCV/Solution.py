from sklearn.datasets import sload
from sklearn.model_selection import GridSearchCV
from sklearn.covariance import LedoitWolf
from sklearn.linear_model import Lasso

# Load your dataset
data = sload('lamb1_l2')
X = data['data']
y = data['target']

# The sparse (precision-weighted) covariance structure to estimate
ledoit_wolf = LedoitWolf(random_state=42)

# The LassoCV estimator for choosing the lasso penalty (alpha).
# If you have a symmetrized covariance matrix, you should use SparseInvCov
lasso_cv = LassoCV(cv=5).fit(X)

# Fit the Lasso estimator with the chosen alpha
lasso = Lasso(alpha=lasso_cv.alpha_)

fit_inverse_cov = ledoit_wolf.fit(X).inverse_covariance_

print(lasso.alpha_)
print(fit_inverse_cov)
