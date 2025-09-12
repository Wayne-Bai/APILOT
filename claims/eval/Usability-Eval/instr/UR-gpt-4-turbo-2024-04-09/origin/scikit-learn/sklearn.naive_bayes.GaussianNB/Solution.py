from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate a random dataset
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Using partial_fit for online updates
classes = np.unique(y_train)
gnb.partial_fit(X_train, y_train, classes=classes)

# Predict the labels of the test set
y_pred = gnb.predict(X_test)

# Evaluate the classifier
accuracy = (y_test == y_pred).mean()
print(f"Accuracy: {accuracy:.2f}")
