from sklearn.naive_bayes import BernoulliNB

# X is the feature matrix and y is the response vector
X = [...]
y = [...]

# Create a BernoulliNB classifier object.
clf = BernoulliNB()

# Train the model using the training sets.
clf.fit(X, y)

# Now, you can predict using this trained model as follows:
# If x_new is a new data point
y_pred = clf.predict(x_new)
