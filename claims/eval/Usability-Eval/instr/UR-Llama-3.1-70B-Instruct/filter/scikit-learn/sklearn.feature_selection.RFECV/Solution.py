# Import necessary libraries
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# Load the dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model and RFECV
model = LogisticRegression(max_iter=1000)
cv = StratifiedKFold(5)

# Initialize RFECV with the model and cross-validation
rfe_cv = RFECV(model, cv=cv)

# Fit the RFECV to the training data
rfe_cv.fit(X_train, y_train)

# Get the optimal number of features
optimal_features = rfe_cv.n_features_

# Transform the data to the optimal number of features
X_train_optimal = rfe_cv.transform(X_train)
X_test_optimal = rfe_cv.transform(X_test)

# Train a new model with the optimal features
model.fit(X_train_optimal, y_train)

# Make predictions
predictions = model.predict(X_test_optimal)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy:.3f}")

# Print the optimal features
print(f"Optimal Features: {optimal_features}")

# Print the support (i.e., the features that were selected)
print(f"Selected Features: {rfe_cv.support_}")

# Print the feature ranking
print(f"Feature Ranking: {rfe_cv.ranking_}")
