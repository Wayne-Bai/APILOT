from sklearn.naive_bayes import MultinomialNB

# Assuming you have your data in X (features) and y (labels)
# Here is an example of random data
import numpy as np

# Generating some random data for demonstration purposes
np.random.seed(42)
X = np.random.randint(2, size=(100, 10))  # 100 samples, 10 features
y = np.random.randint(2, size=100)

# Initializing the Multinomial Naive Bayes classifier
classifier = MultinomialNB()

# Training the classifier
classifier.fit(X, y)

# Predicting the classes for a new set of data
# Assuming X_new is a new set of samples
X_new = np.random.randint(2, size=(10, 10))  # 10 new samples, 10 features
predictions = classifier.predict(X_new)

# Printing the predictions
print("Predictions:", predictions)
