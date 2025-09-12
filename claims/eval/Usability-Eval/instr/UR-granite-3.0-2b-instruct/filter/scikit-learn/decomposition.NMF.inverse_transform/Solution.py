from sklearn.preprocessing import StandardScaler

# Assuming X_transformed is the data that has been transformed
# and X_original is the original data

# Initialize the transformer
scaler = StandardScaler()

# Fit and transform the data
X_transformed = scaler.fit_transform(X_original)

# Now, to transform the data back to its original space, you can use the inverse_transform method
X_original_transformed = scaler.inverse_transform(X_transformed)
