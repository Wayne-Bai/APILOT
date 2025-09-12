from sklearn.naive_bayes import BernoulliNB

# Create an instance of the BernoulliNB classifier
model = BernoulliNB()

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict the labels for the test data
y_pred = model.predict(X_test)

# Evaluate the accuracy of the model
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy}")
