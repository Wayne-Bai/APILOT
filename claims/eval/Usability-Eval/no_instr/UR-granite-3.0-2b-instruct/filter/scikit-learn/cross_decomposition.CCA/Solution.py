from sklearn.crossdecomposition import CanonicalCorrelationAnalysis

# Assuming X and Y are your data matrices
cca = CanonicalCorrelationAnalysis()
cca.fit(X, Y)

# Print the canonical correlations
print("Canonical Correlations:", cca.canonical_coefficients_)

# Print the scores
print("Scores:\n", cca.scores_)

# Print the loadings
print("Loadings:\n", cca.loadings_)
