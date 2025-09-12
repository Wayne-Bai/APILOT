from sklearn.cross_decomposition import PLSRegression
from sklearn.datasets import load_boston
# Load the Boston housing dataset
boston = load_boston()
# Fit a PLS-SVD model to the dataset
pls = PLSRegression(n_components=3)
pls.fit(boston.data, boston.target)
# Transform the dataset using the PLS-SVD model
X_transformed = pls.transform(boston.data)
# Inverse transform the dataset using the PLS-SVD model
X_inverse_transformed = pls.inverse_transform(X_transformed)
