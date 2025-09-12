from sklearn.cross_decomposition import PLSRegression

# Create a PLSRegression object with 2 components
pls = PLSRegression(n_components=2)

# Fit the model to the data
pls.fit(X, y)

# Transform the data
X_transformed = pls.transform(X)

# Fit a linear regression model to the transformed data
lr = LinearRegression()
lr.fit(X_transformed, y)

# Make predictions using the linear regression model
y_pred = lr.predict(X_transformed)
