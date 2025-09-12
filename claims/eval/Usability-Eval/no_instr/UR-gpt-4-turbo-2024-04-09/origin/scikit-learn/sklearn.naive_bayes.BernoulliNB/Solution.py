# Import necessary libraries
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import accuracy_score

# Load a simple example dataset
digits = datasets.load_digits()
# Binarize the data
X = digits.data
X[X > 0] = 1
y = digits.target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize the Bernoulli Naive Bayes classifier
model = BernoulliNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the Bernoulli Naive Bayes classifier: {accuracy:.2f}")
