# Importing necessary libraries
from scipy.special import logit
import numpy as np
from scipy.special import expit
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Generate a multivariate Bernoulli classification problem
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_repeated=0, n_classes=2, n_clusters_per_class=1, random_state=42)

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Bernoulli Naive Bayes classifier
clf = BernoulliNB()

# Train the model using the training sets
clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
# Model Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred))
# Model Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
