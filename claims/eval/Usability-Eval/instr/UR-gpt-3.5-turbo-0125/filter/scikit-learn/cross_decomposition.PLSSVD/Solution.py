
from sklearn.cross_decomposition import PLSRegression
from sklearn.decomposition import TruncatedSVD

# Create a TruncatedSVD object
tsvd = TruncatedSVD(n_components=2)

# Fit the TruncatedSVD model on the data
X_svd = tsvd.fit_transform(X)

# Apply PLSRegression on the reduced data
pls = PLSRegression(n_components=2)
pls.fit(X_svd, y)
