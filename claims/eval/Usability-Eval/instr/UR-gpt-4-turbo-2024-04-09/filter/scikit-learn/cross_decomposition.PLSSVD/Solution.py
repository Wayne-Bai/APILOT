from sklearn.cross_decomposition import PLSRegression

# Define the Partial Least Squares Regression (PLS) model
pls = PLSRegression(n_components=2)

# Example data: X (predictors), Y (responses)
X = [[0., 0.], [1., 2.], [2., 3.], [3., 5.], [5., 8.], [8., 13.]]
Y = [0., 1., 2., 3., 5., 8.]

# Fit the PLS model
pls.fit(X, Y)

# Predict using the PLS model
Y_pred = pls.predict([[1, 5], [2, 4]])

print("Predicted responses:", Y_pred)
