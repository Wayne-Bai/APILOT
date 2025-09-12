
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import load_boston

# Load the Boston housing dataset
boston = load_boston()
X = boston.data
y = boston.target

# Create a Gradient Boosting regressor
gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Train the model
gb.fit(X, y)

# Make predictions on new data
predictions = gb.predict(X)
