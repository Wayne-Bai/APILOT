
from sklearn.naive_bayes import BernoulliNB

# Create an instance of the Bernoulli Naive Bayes classifier
clf = BernoulliNB()

# Train the classifier on training data X_train and labels y_train
clf.fit(X_train, y_train)

# Predict the labels of test data X_test
y_pred = clf.predict(X_test)
