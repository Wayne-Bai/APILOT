from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load Boston housing dataset
boston = load_boston()
X, y = boston.data, boston.target

# Split the dataset into training (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initiate a decision tree regressor
dtr = DecisionTreeRegressor(max_depth=3, random_state=42)

# Train the Decision tree regressor
dtr.fit(X_train, y_train)

# Make predictions using the testing set
predictions = dtr.predict(X_test)

# Evaluate the performance of the model
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")
