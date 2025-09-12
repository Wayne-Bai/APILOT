from sklearn.linear_model import LassoLars
from sklearn.metrics import mean_squared_error
import numpy as np

# Assuming X and y are your feature matrix and target vector

model = LassoLars(alpha=0.1)
model.fit(X, y)

# Calculate the BIC
n = len(y)
p = sum(model.coef_ != 0)
BIC = n * np.log(mean_squared_error(y, model.predict(X))) + p * np.log(n)

print(f'Number of features used: {p}')
print(f'BIC: {BIC}')
