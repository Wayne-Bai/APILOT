from sklearn.linear_model import LogisticRegression

# create an instance of the LogisticRegression classifier
lr = LogisticRegression()

# fit the model to the training data
lr.fit(X_train, y_train)

# predict the labels of the test data
y_pred = lr.predict(X_test)
