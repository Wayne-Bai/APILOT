from sklearn.decomposition import PLSRegression
import numpy as np

# Sample data
X = np.array([[0.1, 0.2, 0.3], 
              [0.4, 0.5, 0.6], 
              [0.7, 0.8, 0.9],
              [1.0, 1.1, 1.2]])

Y = np.array([[1.0], 
              [2.0], 
              [3.0], 
              [4.0]])

# Instantiate PLSRegression
pls = PLSRegression(n_components=2)

# Fit model
pls.fit(X, Y)

# Transform and predict
X_score = pls.transform(X)
Y_pred = pls.predict(X)

print("X Scores:\n", X_score)
print("Predicted Y:\n", Y_pred)
