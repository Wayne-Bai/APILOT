from sklearn.preprocessing import PowerTransformer
import numpy as np

# Let's assume we've already fitted the model and 'X' is our transformed data
# Note: Your data preprocessing step might be different based on your need.
pt = PowerTransformer(method='box-cox')
X = np.array([[1, 2, 3], [4, 5, 6]])
X_transformed = pt.fit_transform(X)

# Now we want to inverse the transformation
X_inverse_transformed = pt.inverse_transform(X_transformed)

print(X_inverse_transformed)
