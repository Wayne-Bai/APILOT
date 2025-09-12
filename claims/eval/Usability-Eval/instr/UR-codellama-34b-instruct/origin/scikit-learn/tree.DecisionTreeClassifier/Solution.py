from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Load your dataset
X = ... # feature values
y = ... # target variable

# Create a decision tree classifier object
clf = DecisionTreeClassifier()

# Train the model using the training data
clf.fit(X, y)

# Use the trained model to make predictions on new data
predictions = clf.predict(new_data)
