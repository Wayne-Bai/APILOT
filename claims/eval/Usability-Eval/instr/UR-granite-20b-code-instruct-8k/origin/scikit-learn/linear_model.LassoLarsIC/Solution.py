from sklearn.linear_model import LassoLarsIC

X = [[0, 0], [1, 1], [2, 2]]  # Replace this with your actual feature matrix
y = [0, 1, 2]  # Replace this with your actual target variable

# Fit the Lasso model with Lars using BIC for model selection
model = LassoLarsIC(criterion='bic')
model.fit(X, y)

# Print the best alpha value and corresponding coefficients
print("Best alpha value:", model.alpha_)
print("Coefficients:", model.coef_)
