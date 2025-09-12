# Importing the necessary libraries
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report

# Assuming we have a dataset (X, y)
X = [
    "This is a movie review text.",
    "The movie was so good.",
    "I did not like the movie.",
    "The plot was exciting with a twist.",
    "I loved the performance of the actors."
]
y = [1, 1, 0, 1, 1]

# Preparing the data for the model by splitting it into training and testing sets
train_text, test_text, train_labels, test_labels = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a TF-IDF vectorizer to transform the text data
vectorizer = TfidfVectorizer()

# Using the vectorizer to fit the training data and transform both the training and testing data
train_vectors = vectorizer.fit_transform(train_text)
test_vectors = vectorizer.transform(test_text)

# Creating a Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Training the classifier using the training data
clf.fit(train_vectors, train_labels)

# Making predictions on the testing data
predictions = clf.predict(test_vectors)

# Evaluating the model using accuracy score and classification report
print("Accuracy:", accuracy_score(test_labels, predictions))
print("Classification Report:")
print(classification_report(test_labels, predictions))
