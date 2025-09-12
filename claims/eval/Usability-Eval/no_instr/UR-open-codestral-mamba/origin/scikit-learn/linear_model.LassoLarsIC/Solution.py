from sklearn.linear_model import LassoLarsIC

# Initialize the LassoLarsIC model with the 'bic' criterion
lasso_bic = LassoLarsIC(criterion='bic')

# Fit the model
# Assuming X_train and y_train are your training data and labels
lasso_bic.fit(X_train, y_train)

# To get the coefficients of the model
coef = lasso_bic.coef_

# or, to predict the output
# Assuming X_test is your test data
y_pred = lasso_bic.predict(X_test)
