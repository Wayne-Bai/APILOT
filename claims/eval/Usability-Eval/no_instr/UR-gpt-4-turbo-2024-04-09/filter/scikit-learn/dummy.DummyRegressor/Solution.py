import numpy as np
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Example synthetic data creation
X = np.random.rand(100, 1) * 100  # 100 feature samples
y = X[:, 0] * 3 + np.random.randn(100) * 10  # Linear relation with some noise

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Dummy Regressor object with strategy as mean
dummy_regressor = DummyRegressor(strategy="mean")

# Fitting the model on the training data
dummy_regressor.fit(X_train, y_train)

# Making predictions
y_pred = dummy_regressor.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Printing predicted values
print(f'Predicted values: {y_pred[:5]}')  # displaying first 5 predictions
