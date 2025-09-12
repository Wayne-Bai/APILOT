from sklearn.cross_decomposition import PLSRegression

# Assuming you have features X and targets Y
# Here is how you can use PLSRegression
pls = PLSRegression(n_components=2)
pls.fit(X, Y)

# Predicting
predictions = pls.predict(X)
