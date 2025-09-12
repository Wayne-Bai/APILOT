from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the data
newsgroups_train = fetch_20newsgroups(subset='train')
newsgroups_test = fetch_20newsgroups(subset='test')

# Convert data into counts
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(newsgroups_train.data)
X_test_counts = vectorizer.transform(newsgroups_test.data)

# Fit the Multinomial Naive Bayes model
clf = MultinomialNB()
clf.fit(X_train_counts, newsgroups_train.target)

# Make predictions
predicted = clf.predict(X_test_counts)

# Evaluate the model
metrics.accuracy_score(newsgroups_test.target, predicted)
