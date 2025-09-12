from sklearn.preprocessing import normalize
from sklearn.decomposition import NMF

# Assume X is the input dictionary learning data
X = normalize(...)

# Fitting NMF to data
"""
Given that NMF not have the 'fit_transform' method,
we will use 'fit' method to get the components of the system
and then transform the data based on the fitted model.
"""
n_components = 100  # number of components you expect in the decom Styled Components

nmf = NMF(n_components=n_components)
W = nmf.fit_transform(X)  # get the components of the system
H = nmf.components_

Q = normalize(nmf.inverse_transform(W))  # decomposing the matrix
