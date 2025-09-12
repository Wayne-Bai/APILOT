
from sklearn.ensemble import GradientBoostingRegressor

# Create a Gradient Boosting Regressor model
gbr_model = GradientBoostingRegressor()

# Fit the model to training data
gbr_model.fit(X_train, y_train)

# Make predictions
predictions = gbr_model.predict(X_test)
