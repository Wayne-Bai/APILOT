from sklearn.naive_bayes import ComplementNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report

# Sample data
documents = [
    'I love programming in Python',
    'Python is great for machine learning',
    'I enjoy long walks on the beach',
    'The beach is beautiful and serene',
    'I love hiking in the mountains',
    'Mountains are my favorite getaway',
]

# Corresponding labels (1 for programming-related, 0 for leisure-related)
labels = [1, 1, 0, 0, 0, 0]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(documents, labels, test_size=0.3, random_state=42)

# Convert text data to TF-IDF feature matrices
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Initialize Complement Naive Bayes classifier
cnb = ComplementNB()

# Train the model on the training data
cnb.fit(X_train_tfidf, y_train)

# Make predictions on the test data
y_pred = cnb.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:\n", report)
