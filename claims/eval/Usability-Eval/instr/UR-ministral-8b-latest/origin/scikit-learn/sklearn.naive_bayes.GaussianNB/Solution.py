from sklearn.naive_bayes import GaussianNB

# Create a GaussianNB object
gnb = GaussianNB()

# Sample data for training
X_train = [[0.5, 1.5], [1.0, 1.0], [1.5, 0.5]]
y_train = [0, 1, 0]

# Fit the model to the training data
gnb.fit(X_train, y_train)
