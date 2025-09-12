from sklearn.cross_decomposition import CCA

# Assuming X and Y are your input data matrices
cca = CCA(n_components=2)
cca.fit(X, Y)

X_scores = cca.transform(X)
Y_scores = cca.transform(Y)

corr = cca.canonical_corurrences_

print("Canonical correlations:", corr)
