from sklearn.cross_decomposition import PLSRegression

# Assuming X is your predictor matrix and y is your response matrix
# X = ...
# y = ...

# Initialize the PLSRegression model
pls = PLSRegression(n_components=2)  # You can adjust the number of components as needed

# Fit the model to the data
pls.fit(X, y)

# Now you can use the model for predictions
# predictions = pls.predict(new_data)
