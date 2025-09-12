# Import necessary libraries
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error

# Load the boston housing dataset
dataset = load_boston()

# Split the dataset into features (X) and target (y)
X = dataset.data
y = dataset.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the HistGradientBoostingRegressor model
model = HistGradientBoostingRegressor()
model.train(X_train, y_train)

# Generate predictions for the testing set
predictions = model.predict(X_test)

# Evaluate the model's performance using mean squared error
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse:.2f}')

# Example of how to input a custom data point for prediction
custom_data_point = [[6.32, 18,  2.31,  0,  0.538,  6.575, 65.2,  4.09,  1, 296, 15.3,  393,  4.98]]
custom_prediction = model.predict(custom_data_point)
print('Prediction for custom data point:', custom_prediction)
