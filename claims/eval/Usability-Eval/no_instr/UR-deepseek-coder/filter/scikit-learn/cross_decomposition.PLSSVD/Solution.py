import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Example dataset
X = np.random.rand(100, 20)  # 100 samples, 20 features
y = np.random.rand(100, 1)   # 100 samples, 1 target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the PLSRegression model
pls = PLSRegression(n_components=2)  # Set the number of components

# Fit the model on the training data
pls.fit(X_train, y_train)

# Predict on the test data
y_pred = pls.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
