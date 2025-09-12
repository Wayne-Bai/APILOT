import numpy as np
import pandas as pd
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sample data generation
np.random.seed(42)
X = np.random.rand(100, 5)  # 100 samples, 5 features
Y = np.random.rand(100, 1)   # 100 samples, 1 target variable

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create PLS Regression model
pls = PLSRegression(n_components=2)

# Fit the model
pls.fit(X_train, Y_train)

# Make predictions
Y_pred = pls.predict(X_test)

# Calculate mean squared error
mse = mean_squared_error(Y_test, Y_pred)
print(f'Mean Squared Error: {mse}')
