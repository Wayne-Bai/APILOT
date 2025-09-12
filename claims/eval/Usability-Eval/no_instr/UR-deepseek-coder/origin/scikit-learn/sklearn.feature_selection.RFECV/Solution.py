import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Generate a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the base estimator
estimator = RandomForestClassifier(random_state=42)

# Initialize RFECV with cross-validation
rfecv = RFECV(estimator, step=1, cv=5, scoring='accuracy')

# Fit the RFECV model to the training data
rfecv.fit(X_train, y_train)

# Transform the training and testing data to include only the selected features
X_train_selected = rfecv.transform(X_train)
X_test_selected = rfecv.transform(X_test)

# Train the estimator on the reduced feature set
estimator.fit(X_train_selected, y_train)

# Predict on the test set
y_pred = estimator.predict(X_test_selected)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy with selected features: {accuracy:.4f}")

# Print the number of selected features
print(f"Number of selected features: {rfecv.n_features_}")
