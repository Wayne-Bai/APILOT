# Import necessary libraries
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn import datasets

# Load some dummy data
boston = datasets.load_boston()
X = boston.data
y = boston.target

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree regressor object
regressor = DecisionTreeRegressor(random_state=0)

# Train the model using the training sets
regressor.fit(X_train, y_train)

# The model is now trained and can be used to make predictions
# For instance, to predict the target for the test set, you can do:
y_pred = regressor.predict(X_test)
