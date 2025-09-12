from sklearn.ensemble import GradientBoostingRegressor

# Create a GradientBoostingRegressor object
gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0)

# Fit the model to the data
gbr.fit(X_train, y_train)

# Make predictions using the model
y_pred = gbr.predict(X_test)
