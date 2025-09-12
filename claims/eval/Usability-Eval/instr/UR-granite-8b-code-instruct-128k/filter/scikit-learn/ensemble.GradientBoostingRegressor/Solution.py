from sklearn.ensemble import GradientBoostingRegressor

# Create a Gradient Boosting model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Train the model using your training data
model.fit(X_train, y_train)

# Make predictions using your test data
predictions = model.predict(X_test)
