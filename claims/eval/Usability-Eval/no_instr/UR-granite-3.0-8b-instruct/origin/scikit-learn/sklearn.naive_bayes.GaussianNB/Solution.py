from sklearn.naive_bayes import GaussianNB

# Initialize the Gaussian Naive Bayes model
gnb = GaussianNB()

# Fit the model to the data
# Assuming X_train and y_train are your training data and labels
gnb.partial_fit(X_train, y_train)

# To update the model with new data
# Assuming X_new and y_new are your new data and labels
gnb.partial_fit(X_new, y_new)
