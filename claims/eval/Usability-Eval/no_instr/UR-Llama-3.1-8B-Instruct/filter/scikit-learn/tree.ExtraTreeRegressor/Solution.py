# Import necessary libraries from scikit-learn
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
import pandas as pd

# Load the Boston housing dataset, this is a simple regression dataset.
dataset = load_boston()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['PRICE'] = dataset.target

# Split the dataset into feature and target array
X = df.iloc[:, :-1]
y = df['PRICE']

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create an instance of ExtraTreesRegressor (An Extremely Randomized Tree Regressor)
model = ExtraTreesRegressor(n_estimators=100, random_state=0, n_jobs=-1)

# Train the model using the training sets
model.fit(X_train, y_train)

# Predict a class for the test set
y_pred = model.predict(X_test)

# Compare the predicted value with actual value
mse = mean_squared_error(y_test, y_pred)

# Print the prediction result
print('Mean Squared Error:', mse)

# Plot the Actual vs Predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Value')
plt.ylabel('Predicted Value')
plt.title('Actual vs Predicted')
plt.show()
