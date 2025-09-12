from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
import numpy as np

# Load the dataset
data = load_iris()
X, y = data.data, data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model
clf.fit(X_train, y_train)

# Create a SelectFromModel object with the fitted RandomForest
selector = SelectFromModel(clf, prefit=True)

# Transform the datasets using the selector
X_train_selected = selector.transform(X_train)
X_test_selected = selector.transform(X_test)

print("Original number of features:", X.shape[1])
print("Reduced number of features:", X_train_selected.shape[1])
