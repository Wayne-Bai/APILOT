from sklearn.preprocessing import StandardScaler

# Example data
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
scaler = StandardScaler()

# Fit the scaler on the data
scaler.fit(data)

# Transform the data
transformed_data = scaler.transform(data)

# Inverse the transformation to return the original data
inverse_transformed_data = scaler.inverse_transform(transformed_data)

# Print the shape of the original and inverse transformed data
print(f"Original data shape: {data[0]}")
print(f"Inverse transformed data shape: {inverse_transformed_data}")
