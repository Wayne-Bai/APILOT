from sklearn.preprocessing import StandardScaler

# Assuming you have already fitted the StandardScaler on your data
scaler = StandardScaler()

# Transform data back to original space
transformed_data = scaler.inverse_transform(data)
