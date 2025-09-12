
# Importing the necessary libraries
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier

# Create an instance of the Gradient Boosting Classifier
clf = GradientBoostingClassifier()

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
predictions = clf.predict(X_test)
