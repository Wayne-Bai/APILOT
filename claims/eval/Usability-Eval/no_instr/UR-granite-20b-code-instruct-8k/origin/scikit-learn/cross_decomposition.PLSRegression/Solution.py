from sklearn.cross_decomposition import PLSRegression

# Initialize the PLS Regression model
model = PLSRegression()

# Fit the model to the data
model.fit(X, y)

# Predict the target variable values for a new set of data
y_pred = model.predict(X_new)
