import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import ComplementNB

# Sample text data
documents = [
    "This is a good book",
    "This is a bad book",
    "I like this book",
    "I do not like this book",
    "Good books are my favorite",
    "Bad books are not my favorite"
]

# Corresponding labels
# 1 for positive sentiment, 0 for negative sentiment
labels = [1, 0, 1, 0, 1, 0]

# Convert the text data into numerical data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.5, random_state=42)

# Initialize the Complement Naive Bayes classifier
cnb = ComplementNB()

# Train the classifier
cnb.fit(X_train, y_train)

# Predict the labels for the test data
y_pred = cnb.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)

# Output the accuracy
print("Accuracy:", accuracy)
