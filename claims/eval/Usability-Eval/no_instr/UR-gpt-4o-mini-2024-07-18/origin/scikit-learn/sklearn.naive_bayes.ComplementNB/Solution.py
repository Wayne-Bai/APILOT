from sklearn.naive_bayes import ComplementNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer

# Sample dataset
X = ["text data sample1", "text data sample2", "text data sample3"]
y = [0, 1, 0]  # Sample labels (imbalanced)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data into numerical format
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Initialize Complement Naive Bayes classifier
complement_nb = ComplementNB()

# Fit the model on the training data
complement_nb.fit(X_train_vectorized, y_train)

# Make predictions on the test data
y_pred = complement_nb.predict(X_test_vectorized)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:\n", report)
