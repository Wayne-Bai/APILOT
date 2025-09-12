# Import necessary libraries
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

# Load dataset
data = datasets.load_iris().data

# Initialize StandardScaler
scaler = StandardScaler()

# Fit and transform the data
data_scaled = scaler.fit_transform(data)

# Inverse transform the data back to its original space
data_original = scaler.inverse_transform(data_scaled)
