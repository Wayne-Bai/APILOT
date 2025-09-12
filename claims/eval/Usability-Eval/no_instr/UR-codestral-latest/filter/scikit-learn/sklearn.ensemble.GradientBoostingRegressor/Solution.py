# Import the necessary module
from sklearn.ensemble import GradientBoostingRegressor

# Assume X and y are the feature matrix and response vector respectively
# and have been already defined

# Create a GradientBoostingRegressor model
gb_regressor = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0, loss='ls')

# Fit the model
gb_regressor.fit(X, y)

# Now, the model is ready to use for predictions
# Predict the response for new observations
y_pred = gb_regressor.predict(X_new)
