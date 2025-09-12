from sklearn.preprocessing import MinMaxScaler

# Sample data
data = [[1, 2], [3, 4], [5, 6]]

# Create a scaler instance
scaler = MinMaxScaler()

# Fit and transform the data
transformed_data = scaler.fit_transform(data)

# Suppose we want to inverse the transformation
inverse_transformed_data = scaler.inverse_transform(transformed_data)

# Get the inverse transformed data as a vector of size n_features
n_features = transformed_data.shape[1]
inverse_vector = inverse_transformed_data[0]  # Select the first sample as a vector

print(inverse_vector)
