from sklearn.preprocessing import StandardScaler
import numpy as np

# Assuming we have some data, X to scale
X = np.array([[1., 2.], [3., 4.], [5., 6.]])
print(f'Original Data: \n{X}')

# Define Scaler
scaler = StandardScaler()

# Fit and transform data
X_scaled = scaler.fit_transform(X)
print(f'\nScaled Data: \n{X_scaled}')

# Inverse transformation
X_original = scaler.inverse_transform(X_scaled)
print(f'\nOriginal Data after inverse transformation: \n{X_original}')
