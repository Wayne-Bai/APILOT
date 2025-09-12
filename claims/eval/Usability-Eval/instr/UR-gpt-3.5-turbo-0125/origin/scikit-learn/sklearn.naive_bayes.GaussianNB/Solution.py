
from sklearn.naive_bayes import GaussianNB

# Initialize Gaussian Naive Bayes model
gnb = GaussianNB()

# Perform online updates using partial_fit
# X_train and y_train are the training data
gnb.partial_fit(X_train, y_train, classes=np.unique(y_train))
