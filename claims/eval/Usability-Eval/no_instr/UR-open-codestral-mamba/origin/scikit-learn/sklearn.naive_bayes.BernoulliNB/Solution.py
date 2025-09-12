# import necessary libraries
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import classification_report

# Load the '20newsgroups' dataset
newsgroups_data = fetch_20newsgroups(subset='train')

# Initialize CountVectorizer instance
count_vect = CountVectorizer(stop_words='english')

# Transform the newsgroups data
X_train_counts = count_vect.fit_transform(newsgroups_data.data)

# Initialize BernoulliNB instance
bernoulli_nb = BernoulliNB()

# Fit the model
bernoulli_nb.fit(X_train_counts, newsgroups_data.target)

# Test the model with the same dataset
predictions = bernoulli_nb.predict(X_train_counts)

# Print the classification report
print(classification_report(newsgroups_data.target, predictions))
