from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

# Load Boston housing dataset
boston = load_boston()

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.3, random_state=42)

# Train a decision tree regressor on the training data
dt = DecisionTreeRegressor()
dt.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = dt.predict(X_test)

# Evaluate the performance of the model using mean squared error
mse = ((y_test - y_pred) ** 2).mean()
print("Mean squared error: ", mse)
