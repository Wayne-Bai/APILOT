
from sklearn.cross_decomposition import CCA

# Assume X and Y are your two multivariate datasets
cca = CCA(n_components=2)
cca.fit(X, Y)

# Transform the datasets into the CCA subspace
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
