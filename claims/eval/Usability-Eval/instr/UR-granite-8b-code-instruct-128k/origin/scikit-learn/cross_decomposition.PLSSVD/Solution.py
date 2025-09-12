from sklearn.decomposition import PartialLeastSquares

# Assuming X is your input data and y is your target variable

# Initialize the PartialLeastSquares object
pls = PartialLeastSquares(n_components=10)

# Fit the model to the data
pls.fit(X, y)

# Transform the data
X_transformed = pls.transform(X)

# Use the transformed data for further analysis
