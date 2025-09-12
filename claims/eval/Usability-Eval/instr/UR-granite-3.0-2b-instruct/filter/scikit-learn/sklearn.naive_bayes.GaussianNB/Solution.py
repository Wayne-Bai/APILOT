from sklearn.naive_bayes import GaussianNB

# Importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Loading dataset
iris = load_iris()
X = iris.data
y = iris.target

# Splitting dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Creating a Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Training the model using the training sets
gnb.fit(X_train, y_train)

# Predicting the response for test dataset
y_pred = gnb.predict(X_test)

# Model evaluation
accuracy = gnb.score(X_test, y_test)
print("Accuracy:", accuracy)
