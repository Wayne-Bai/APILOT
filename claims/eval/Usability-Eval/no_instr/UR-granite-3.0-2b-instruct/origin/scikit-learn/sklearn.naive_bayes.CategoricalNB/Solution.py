from sklearn.naive_bayes import GaussianNB

# Assuming X is your features and y is your target variable
# X = ...
# y = ...

# Initialize the Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Fit the classifier with your data
gnb.fit(X, y)

# Now you can use the classifier to make predictions
# For example, to predict the target variable for a new sample x
# y_pred = gnb.predict([x])
