from sklearn.crossdecomp import CanonicalCorrelationAnalysis

# Assuming X and Y are your datasets
CCA = CanonicalCorrelationAnalysis()
CCA.fit(X, Y)

# Print the results
print("Canonical Correlation Coefficients:")
print(CCA.canonical_correlations_)

# Print the loadings
print("Loadings:")
print(CCA.loadings_)

# Print the scores
print("Scores:")
print(CCA.scores_)
