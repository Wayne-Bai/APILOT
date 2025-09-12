# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

# Generate some random data for demonstration purposes
np.random.seed(0)
X = np.random.rand(100, 3)
y = 3 * X[:, 0] + 2 * X[:, 1] + 4 * X[:, 2] + np.random.rand(100)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(X, columns=['Feature1', 'Feature2', 'Feature3'])
df['Target'] = y

# Split the data into features and target
X = df[['Feature1', 'Feature2', 'Feature3']]
y = df['Target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a DecisionTreeRegressor
dt_regressor = DecisionTreeRegressor(random_state=42)
dt_regressor.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = dt_regressor.predict(X_test)

# Evaluate the model using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)

# Print out the features and their corresponding importance
print("Feature Importances:")
print(dt_regressor.feature_importances_)
