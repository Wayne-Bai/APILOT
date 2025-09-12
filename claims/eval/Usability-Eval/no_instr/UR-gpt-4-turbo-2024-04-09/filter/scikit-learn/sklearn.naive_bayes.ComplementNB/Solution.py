from sklearn.naive_bayes import ComplementNB
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate a synthetic dataset (you can replace this with your actual dataset)
X, y = make_classification(n_samples=1000, n_features=20, weights=[0.9, 0.1], flip_y=0.05, random_state=42)

# Split the generated data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating an instance of Complement Naive Bayes Classifier
cnb = ComplementNB()

# Fit the model
cnb.fit(X_train, y_train)

# Predicting the labels for test set
y_pred = cnb.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
