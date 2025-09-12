from sklearn.cross_decomposition import PLSRegression
import numpy as np

# Sample data
X = np.array([[0., 0., 1.], [1., 0., 0.], [2., 2., 2.], [3., 5., 4.]])
Y = np.array([[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]])

# Create PLSRegression model
pls = PLSRegression(n_components=2)

# Fit the model
pls.fit(X, Y)

# Predict using the model
Y_pred = pls.predict(X)

print("Predicted values:")
print(Y_pred)
