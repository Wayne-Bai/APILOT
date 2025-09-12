# Import required libraries
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# Data preprocessing
X = ['word1', 'word2', 'word3', 'word4']  # Replace with actual data
y = ['class1', 'class2', 'class1', 'class2']  # Replace with actual data

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data to numerical data using Bag of words
count_vectorizer = CountVectorizer()
X_train_counts = count_vectorizer.fit_transform(X_train)
X_test_counts = count_vectorizer.transform(X_test)

# Apply Naive Bayes classifier for multinomial models
naive_bayes_classifier = MultinomialNB()
naive_bayes_classifier.fit(X_train_counts, y_train)
y_pred = naive_bayes_classifier.predict(X_test_counts)

# Calculate Accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
