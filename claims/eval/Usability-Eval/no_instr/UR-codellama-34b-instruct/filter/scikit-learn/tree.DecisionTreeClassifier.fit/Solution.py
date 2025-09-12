
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Load your dataset
X = ... # input features
y = ... # target variable

# Create the decision tree classifier object
clf = DecisionTreeClassifier()

# Train the model using the training data
clf.fit(X, y)

# Use the trained model to make predictions on new data
predictions = clf.predict(new_data)
