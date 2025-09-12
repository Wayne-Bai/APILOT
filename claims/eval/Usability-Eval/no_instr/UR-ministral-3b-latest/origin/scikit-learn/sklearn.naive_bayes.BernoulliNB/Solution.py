from sklearn.naive_bayes import BernoulliNB

# example code to check output

# create some example data
X = [[0, 1], [1, 1], [0, 0], [1, 0]]
y = [0, 1, 0, 1]

# create a BernoulliNB object
clf = BernoulliNB()

# fit the model
clf.fit(X, y)

# predict from test data
X_test = [[0, 1], [1, 1]]
y_pred = clf.predict(X_test)

y_pred
