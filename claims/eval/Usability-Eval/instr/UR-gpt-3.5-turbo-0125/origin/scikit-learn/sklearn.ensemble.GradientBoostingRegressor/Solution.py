
from sklearn.ensemble import GradientBoostingRegressor

# Create a Gradient Boosting Regressor model
params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2,
          'learning_rate': 0.01, 'loss': 'ls'}
model = GradientBoostingRegressor(**params)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)
