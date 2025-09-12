from sklearn.naive_bayes import GaussianNB

# Create a Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Assume X is your features and y is your target variable
# gnb.fit(X, y)  # This will train the model on the entire dataset

# For online updates, you can use partial_fit
gnb.partial_fit(X_new, y_new, classes=gnb.classes_)
