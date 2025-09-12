from sklearn.naive_bayes import GaussianNB

# Initialize the GaussianNB classifier
gnb = GaussianNB()

# For online learning, 'partial_fit' can be called for each mini-batch of data.
# Each call will update the internal parameter estimates.
mini_batch_size = 100  # modify this size according to your data
for i in range(0, len(data), mini_batch_size):
    X_mini = data[i:i + mini_batch_size]
    y_mini = labels[i:i + mini_batch_size]
    gnb.partial_fit(X_mini, y_mini, classes=np.unique(labels))
