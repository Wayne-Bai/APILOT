# Importing necessary libraries
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Assuming we have a dataset X and target values y
# Here, we will split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating the DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=42)

# Training the regressor with the training data
regressor.fit(X_train, y_train)

# Making predictions on the testing set
predictions = regressor.predict(X_test)

# Evaluating the performance of the regressor with mean squared error
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
