import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import plot_precision_recall_curve

# Generate a random dataset with 100 samples, 20 features, 5 informative features and binary outcomes
X, y = make_classification(n_samples=100, n_features=20, n_informative=5, n_classes=2, n_redundant=0, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Define a logistic regression model
model = LogisticRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Plot the precision-recall curve
plot_precision_recall_curve(model, X_test, y_test)
