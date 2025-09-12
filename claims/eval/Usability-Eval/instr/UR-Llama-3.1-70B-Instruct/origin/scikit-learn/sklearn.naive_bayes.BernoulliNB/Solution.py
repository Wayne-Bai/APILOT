# Import necessary libraries
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import make_multinomial
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Generate a random multinomial dataset
X, y = make_multinomial(n_samples=1000, n_features=100, n_classes=3, random_state=42)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Multinomial Naive Bayes classifier
clf = MultinomialNB()
clf.partial_fit(X_train, y_train, classes=[0, 1, 2]) # use partial_fit with classes for safe usage instead of fit 

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the classifier's performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
