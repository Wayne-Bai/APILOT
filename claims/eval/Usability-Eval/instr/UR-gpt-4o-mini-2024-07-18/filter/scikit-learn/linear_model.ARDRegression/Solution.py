
from sklearn.linear_model import BayesianARD
import numpy as np

# Sample data
X = np.random.rand(100, 5)  # 100 samples, 5 features
y = np.random.rand(100)      # 100 target values

# Create and fit the Bayesian ARD regression model
model = BayesianARD()
model.fit(X, y)

# After fitting, you can access the model's parameters
weights = model.coef_
alpha = model.alpha_
lambdas = model.lambda_

print("Weights:", weights)
print("Alpha (precision of noise):", alpha)
print("Lambdas (precisions of weights):", lambdas)
