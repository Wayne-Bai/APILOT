
from sklearn.linear_model import BayesianRidge

# Assume X is the input features and y is the target variable
model = BayesianRidge()
model.fit(X, y)

# The weights of the regression model are stored in the 'coef_' attribute
weights = model.coef_

# The parameters lambda and alpha are stored in the 'alpha_' and 'lambda_' attributes, respectively
lambda_params = model.lambda_
alpha_params = model.alpha_
