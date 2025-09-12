
from sklearn.linear_model import BayesianRidge

# Create a Bayesian Ridge model
model = BayesianRidge()

# Fit the model
model.fit(X_train, y_train)

# Use the model to make predictions
predictions = model.predict(X_test)
