from sklearn.decomposition import TruncatedSVD
from sklearn.cross_decomposition import PLSRegression

# Assuming X is your feature matrix and y is your target variable
svd = TruncatedSVD(n_components=k)  # k is the number of components you want to keep
X_svd = svd.fit_transform(X)

# Fit PLSRegression model
pls = PLSRegression(n_components=k)
pls.fit(X_svd, y)
