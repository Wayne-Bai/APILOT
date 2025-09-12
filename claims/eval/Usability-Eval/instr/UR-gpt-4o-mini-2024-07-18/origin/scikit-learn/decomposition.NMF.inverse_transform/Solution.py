from sklearn.preprocessing import StandardScaler

# Example data
data = [[1, 2], [3, 4], [5, 6]]

# Initialize and fit StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Transforming the scaled data back to the original space
original_data = scaler.inverse_transform(scaled_data)

# Display the original data
print(original_data)
