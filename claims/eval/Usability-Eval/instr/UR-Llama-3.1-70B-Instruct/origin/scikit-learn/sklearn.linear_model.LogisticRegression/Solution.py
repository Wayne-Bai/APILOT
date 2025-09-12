# Importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression as LR
from sklearn import metrics
import numpy as np

# Sample dataset
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([0, 0, 1, 1, 1])

# Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing features by removing the mean and scaling to unit variance
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training a logistic regression model on the training set
classifier = LR(max_iter=1000)
classifier.fit(X_train, y_train)

# Making predictions on the test set
y_pred = classifier.predict(X_test)
y_pred_prob = classifier.predict_proba(X_test)

# Model Accuracy: how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))

# Predicting the response for a new input
new_input = [[10, 12]]
new_input = sc.transform(new_input)
new_pred = classifier.predict(new_input)
print("Prediction for new input:", new_pred)
