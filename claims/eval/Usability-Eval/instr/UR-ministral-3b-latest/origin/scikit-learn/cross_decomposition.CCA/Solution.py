from sklearn.cross_decomposition import CanonicalCorrelationAnalysis
import numpy as np

# Assuming X and y are your datasets
X = ...
y = ...

cca = CanonicalCorrelationAnalysis(n_components=2)  # Change n_components as per your requirement
cca.fit(X, y)

# Extracting the canonical correlations and the loadings
cc = cca.canonical_vars_
loadings_X = cca.loadings_[0]
loadings_y = cca.loadings_[1]

cc, loadings_X, loadings_y
