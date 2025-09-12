import numpy as np
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# Example dataset
X = np.random.rand(100, 1)
Y = np.random.rand(100)

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create and train the SVR model
svr_model = SVR(kernel='rbf', C=1.0, epsilon=0.1)
svr_model.fit(X_scaled, Y)

# Make predictions
X_scaled_pred = X_scaled[:, np.newaxis]  # Adjust shape for SVR input
Y_pred = svr_model.predict(X_scaled_pred)

# Calculate the coefficient of determination (R^2 score)
r2 = metrics.r2_score(Y, Y_pred)

print(f"R^2 Score: {r2}")

# Plot the decision boundary (for better visualization)
import matplotlib.pyplot as plt

plt.scatter(X, Y, color='black', label='Data points')
plt.plot(X, Y_pred, color='blue', label='Fitted line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
