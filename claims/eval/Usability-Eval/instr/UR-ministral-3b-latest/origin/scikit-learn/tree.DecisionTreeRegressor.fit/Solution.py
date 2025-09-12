import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics

# Load Iris dataset
iris = sklearn.datasets.load_iris()
housing = iris['data']
housing = housing[:40]

# Create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(housing, iris['target'], random_state=0)

# Create the decision tree regressor
tree = DecisionTreeRegressor()
tree.fit(X_train, y_train)

# Make predictions
y_pred = tree.predict(X_test)

# Calculate the mean squared error
mse = metrics.mean_squared_error(y_test, y_pred)

print("Mean Squared Error:", mse)
