from sklearn.preprocessing import StandardScaler

# Assume `scaled_data` is the data that has been scaled
# Create an instance of StandardScaler
scaler = StandardScaler()

# Fit the scaler on the original data (not shown here)
# original_data = ...

# To transform back to the original space, we use the inverse_transform method
# scaled_data = scaler.fit_transform(original_data) # This would be done before
original_space_data = scaler.inverse_transform(scaled_data)
