from sklearn.cross_decomposition import PLSRegression

# Assume X and Y are your data matrices
# X and Y should have the same number of samples
pls = PLSRegression(n_components=2)
pls.fit(X, Y)

# To transform the data
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)

# The transformed data can be used to calculate the Canonical Correlations
