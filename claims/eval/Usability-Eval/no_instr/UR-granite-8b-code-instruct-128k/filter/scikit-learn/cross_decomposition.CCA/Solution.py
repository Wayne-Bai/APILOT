from sklearn.cross_decomposition import CCA

# Assume that X and Y are your input data
cca = CCA()
cca.fit(X, Y)

# The transformed X and Y can be obtained using the transform() method
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
