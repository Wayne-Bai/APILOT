from sklearn.decomposition import TruncatedSVD
from sklearn.cross_decomposition import PLSRegression

# Assuming X and y are your features and target variable
# X = ...
# y = ...

# Initialize TruncatedSVD
svd = TruncatedSVD(n_components=2)

# Fit and transform X
X_svd = svd.fit_transform(X)

# Initialize PLSRegression
pls = PLSRegression(n_components=2)

# Fit and transform X and y
X_pls, y_pls = pls.fit_transform(X, y)
