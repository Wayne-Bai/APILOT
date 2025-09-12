# Importing the necessary libraries
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Assuming you have a dataset, it's split into features (X) and target (y)
# X, y = load_your_data()

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Create Decision Tree regressor object
regressor = DecisionTreeRegressor(random_state = 42)

# Train the model using the training sets
regressor.fit(X_train, y_train)

# Predicting a new result with Test Set
y_pred = regressor.predict(X_test)

# Evaluating the Model Performance
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)
