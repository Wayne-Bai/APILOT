from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
# Generate some regression data
X, y = make_regression(n_samples=1000, n_features=4, noise=0.01)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a Gradient Boosting regressor
gml = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1)
# Fit the model to the training data
gml.fit(X_train, y_train)
# Make predictions on the testing data
gml_predictions = gml.predict(X_test)
# Evaluate the model
gml_score = gml.score(X_test, y_test)
print("Gradient Boosting Regressor Score:", gml_score)
