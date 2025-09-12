from sklearn.cross_decomposition import PLSRegression

# Create the PLSRegression object
pls = PLSRegression(n_components=2)

# Fit to data
pls.fit(X, Y)

# Predict
Y_pred = pls.predict(X)
