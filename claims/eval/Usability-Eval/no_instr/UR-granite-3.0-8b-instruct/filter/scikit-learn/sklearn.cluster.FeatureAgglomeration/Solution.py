from sklearn.feature_selection import VarianceThreshold

# Assuming X is your feature matrix
selector = VarianceThreshold(threshold=0.5)
X_new = selector.fit_transform(X)
