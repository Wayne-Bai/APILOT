from sklearn.preprocessing import StandardScaler

def sparse_inverse_covariance_estimation(data):
    # Standardize the data
    scaler = StandardScaler()
    data_normalized = scaler.fit_transform(data)

    # ... rest of the function implementation goes here ...
