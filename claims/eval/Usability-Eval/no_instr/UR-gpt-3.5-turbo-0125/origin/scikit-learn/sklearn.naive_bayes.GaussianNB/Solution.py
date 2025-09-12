
from sklearn.naive_bayes import GaussianNB

# Create an instance of Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Perform online updates to model parameters via partial_fit
# X_train is the training input samples and y_train is the target values
gnb.partial_fit(X_train, y_train, classes=np.unique(y_train))
