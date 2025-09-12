# Import scikit-learn
from sklearn.linear_model import LassoLarsIC

# Initialize the LassoLarsIC model with "bic" or "aic" as the criterion
model = LassoLarsIC(criterion="bic")

# Fit the model to the data
model.fit(X, y)

# Print the value of the criterion for the selected model
print(model.criterion_)

# Print the coefficients of the selected model
print(model.coef_)
