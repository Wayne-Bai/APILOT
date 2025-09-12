# Import required libraries from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import datasets
import pandas as pd
import numpy as np

# Load iris dataset
iris = datasets.load_iris()

# Create a DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Separate features and target variable
X = df.drop('target', axis=1)
y = df['target']

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train the model
clf.fit(X_train, y_train)

# Make predictions
predictions = clf.predict(X_test)

# Evaluate the model
accuracy = metrics.accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Make predictions on new data
new_data = pd.DataFrame([[5.1, 3.5, 1.4, 0.2], [7.0, 3.2, 4.7, 1.4]])
new_data_predictions = clf.predict(new_data)
print("Predictions on new data:", new_data_predictions)
