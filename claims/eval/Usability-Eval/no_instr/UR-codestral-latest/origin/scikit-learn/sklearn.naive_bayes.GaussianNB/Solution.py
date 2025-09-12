from sklearn.naive_bayes import GaussianNB

# Create a Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Fit the model to the data
# This can also be done incrementally for online learning using the partial_fit method
gnb.partial_fit(X_train, y_train, classes=np.unique(y_train))

# For making predictions
y_pred = gnb.predict(X_test)
