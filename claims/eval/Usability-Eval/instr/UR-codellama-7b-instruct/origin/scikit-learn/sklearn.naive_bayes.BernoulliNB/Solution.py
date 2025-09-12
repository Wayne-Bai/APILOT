
from sklearn.naive_bayes import MultinomialNB
import numpy as np

# Load dataset
X = np.array([[0, 1], [2, 1], [3, 1]])
y = np.array([1, 2, 3])

# Create Naive Bayes classifier
nb = MultinomialNB()

# Train the classifier
nb.fit(X, y)

# Print trained model
print(nb)
