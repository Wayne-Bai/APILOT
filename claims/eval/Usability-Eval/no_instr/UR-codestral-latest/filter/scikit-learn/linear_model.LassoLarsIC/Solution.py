# Import necessary libraries
from sklearn.linear_model import LassoLarsIC
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# Generate some data
X, y = make_regression(n_samples=100, n_features=25, noise=0.1)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an instance of LassoLarsIC with BIC as the criteria for model selection
lasso_bic = LassoLarsIC(criterion='bic')

# Fit the model to the training data
lasso_bic.fit(X_train, y_train)

# Compute the BIC
bic = lasso_bic.score(X_train, y_train)
print("The BIC Score for BIC LARS model:", bic)

# Alternatively, use AIC for model selection instead
lasso_aic = LassoLarsIC(criterion='aic')
lasso_aic.fit(X_train, y_train)
aic = lasso_aic.score(X_train, y_train)
print("The AIC Score for AIC LARS model:", aic)
