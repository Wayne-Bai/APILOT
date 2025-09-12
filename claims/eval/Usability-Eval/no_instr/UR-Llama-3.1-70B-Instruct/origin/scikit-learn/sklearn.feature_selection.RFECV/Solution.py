# Import necessary libraries
from sklearn.feature_selection import RecursiveFeatureElimination
from sklearn.feature_selection import RFECV
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_friedman1
from sklearn.linear_model import Lasso
from sklearn.metrics import accuracy_score, make_scorer, mean_squared_error
from sklearn.svm import SVR
import numpy as np

# Generate a sample dataset (you can replace this with your actual dataset)
X, y = make_friedman1(n_samples=50, n_features=10, random_state=0)

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Recursive Feature Elimination with cross-validation
estimator = SVR(kernel="linear")
selector = RFECV(estimator, step=1, cv=5)

# Fit the selector to the training data
selector.fit(X_train, y_train)

# Print the support (selected features) and the ranking of features
print("Support:", selector.support_)
print("Feature ranking:", selector.ranking_)

# Transform the data to only include the selected features
X_train_selected = selector.transform(X_train)
X_test_selected = selector.transform(X_test)

# Train a model using the selected features and evaluate its performance
estimator.fit(X_train_selected, y_train)
y_pred = estimator.predict(X_test_selected)

# Evaluate the performance of the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
