# Import necessary libraries
from sklearn.naive_bayes import ComplementNB
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Generate a sample dataset
X, y = make_blobs(n_samples=1000, centers=2, n_features=2, cluster_std=1.05, random_state=40)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Complement Naive Bayes classifier (used instead of GaussianNB for online updates)
clf = ComplementNB()

# Perform online updates to model parameters via partial_fit
clf.partial_fit(X_train, y_train, classes=np.unique(y_train))

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
