from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Assuming X is your feature matrix and y is your target variable
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Initialize the Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Train the classifier
clf.fit(X_vectorized, y)

# Make predictions
y_pred = clf.predict(X_vectorized)

# Calculate accuracy
accuracy = accuracy_score(y, y_pred)
print(f"Accuracy: {accuracy}")
