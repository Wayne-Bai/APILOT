
import numpy as np
from sklearn.naive_bayes import MultinomialNB

# Load the data
X = ...  # Replace with your data matrix
y = ...  # Replace with your target vector

# Create a MBNB classifier object
clf = MultinomialNB()

# Train the model on the data
clf.fit(X, y)

# Make predictions on the test set
predictions = clf.predict(X)
