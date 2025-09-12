from sklearn.linear_model import BayesianRidge
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import numpy as np

# Generate a synthetic dataset
X, y = make_regression(n_samples=100, n_features=20, noise=0.1)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Bayesian ridge regression model
model = make_pipeline(BayesianRidge())

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)
