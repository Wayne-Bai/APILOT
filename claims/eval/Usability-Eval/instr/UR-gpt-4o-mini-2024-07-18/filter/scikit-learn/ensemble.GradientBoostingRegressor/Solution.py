import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Sample data creation
# X represents the features and y represents the target variable
X = np.random.rand(100, 5)  # 100 samples, 5 features
y = X @ np.array([1.5, -2.0, 1.0, 2.5, -1.0]) + np.random.normal(0, 0.1, 100)  # Linear combination with noise

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Gradient Boosting Regressor
gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Fitting the model on the training data
gbr.fit(X_train, y_train)

# Making predictions on the test data
y_pred = gbr.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
