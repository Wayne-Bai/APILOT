
# Import necessary libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import pandas as pd

# Let's assume we have a dataset (X, y) stored in a pandas DataFrame
data = {
    'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    'feature2': [2, 3, 4, 5, 6, 7, 1, 2, 3, 4],
    'target': [0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

# Split dataset into features and target variable
X = df[['feature1', 'feature2']]
y = df['target']

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a Decision Tree classifier object
clf = DecisionTreeClassifier(random_state=0)

# Train the classifier using the training features (X_train) and target (y_train)
clf = clf.fit(X_train, y_train)

# Make predictions on the test features (X_test)
y_pred = clf.predict(X_test)

# Model Accuracy
# Print out the total number of samples
print("Total number of samples:", len(y_test))

# Model Accuracy
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)

# Classification metrics
print("Classification Metrics:")
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 score: ", metrics.f1_score(y_test, y_pred))
