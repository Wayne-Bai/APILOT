from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import make_classification

# Create a dataset
X, y = make_classification(n_samples=100, n_features=20, random_state=42)

# Split dataset into initial training and subsequent samples
X_initial, X_online = X[:80], X[80:]
y_initial, y_online = y[:80], y[80:]

# Initialize the Gaussian Naive Bayes model
gnb = GaussianNB()

# Initially fit the model with the initial dataset
gnb.fit(X_initial, y_initial)

# Online updates with partial_fit
for X_batch, y_batch in zip([X_online], [y_online]):
    # Update the model incrementally
    gnb.partial_fit(X_batch, y_batch, classes=np.unique(y))

# Test the model on new samples
new_samples = X_online[:5]
predictions = gnb.predict(new_samples)

# Show predictions
print(predictions)
