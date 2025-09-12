
from sklearn.ensemble import ExtraTreesRegressor

# Create an Extra Trees Regressor model
model = ExtraTreesRegressor()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)
