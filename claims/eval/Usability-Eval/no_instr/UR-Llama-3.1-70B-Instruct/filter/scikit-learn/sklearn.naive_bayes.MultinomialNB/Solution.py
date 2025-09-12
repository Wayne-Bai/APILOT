# Import necessary libraries
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

# Load dataset
newsgroups_train = fetch_20newsgroups(subset='train')
newsgroups_test = fetch_20newsgroups(subset='test')

# Create a pipeline with CountVectorizer and Multinomial Naive Bayes classifier
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('clf', MultinomialNB())
])

# Split the data into training and test sets
X_train, X_val, y_train, y_val = train_test_split(newsgroups_train.data, newsgroups_train.target, test_size=0.2, random_state=42)

# Train the model on the training data
pipeline.fit(X_train, y_train)

# Make predictions on the validation set
y_pred_val = pipeline.predict(X_val)

# Evaluate the model on the validation set
print("Validation Accuracy:", accuracy_score(y_val, y_pred_val))
print("Validation Confusion Matrix:\n", confusion_matrix(y_val, y_pred_val))
print("Validation Classification Report:\n", classification_report(y_val, y_pred_val))

# Make predictions on the test set
y_pred_test = pipeline.predict(newsgroups_test.data)

# Evaluate the model on the test set
print("Test Accuracy:", accuracy_score(newsgroups_test.target, y_pred_test))
print("Test Confusion Matrix:\n", confusion_matrix(newsgroups_test.target, y_pred_test))
print("Test Classification Report:\n", classification_report(newsgroups_test.target, y_pred_test))
