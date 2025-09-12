from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Example data
data = [[0, 0], [1, 1], [2, 2]]

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Transform back to original space
original_data = scaler.inverse_transform(scaled_data)

print("Original Data:", data)
print("Scaled Data:", scaled_data)
print("Transformed Back Data:", original_data)
