# Import necessary libraries from scikit-learn
from sklearn import preprocessing
import numpy as np

# Generate sample data
X = np.array([[1, 2], [3, 4], [5, 6]])

# Create an instance of StandardScaler (you can use any scaler or transformer you need)
scaler = preprocessing.StandardScaler()

# Fit the scaler to the data and transform it
X_scaled = scaler.fit_transform(X)

# Transform data back to its original space by using inverse_transform (Now using new API 'transform') 
X_back_to_original = scaler.transform(X_scaled)

print("Original Data:")
print(X)
print("Scaled Data:")
print(X_scaled)
print("Data back to original space:")
print(X_back_to_original)
