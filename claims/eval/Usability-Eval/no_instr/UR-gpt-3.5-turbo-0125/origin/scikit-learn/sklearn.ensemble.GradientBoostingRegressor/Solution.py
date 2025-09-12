
from sklearn.ensemble import GradientBoostingRegressor

# Create a Gradient Boosting Regressor model
model = GradientBoostingRegressor()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)
