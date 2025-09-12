# Importing necessary libraries
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import numpy as np

# Generating a random classification dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, random_state=42)

# Splitting dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Training the classifier using the training data
gnb.fit(X_train, y_train)

# Making predictions using the testing data
y_pred = gnb.predict(X_test)

# Performing online updates to model parameters via partial_fit
# Let's assume we have some new data
new_X = np.random.rand(50, 10)
new_y = np.random.randint(2, size=50)

# Performing partial fit
gnb.partial_fit(new_X, new_y, np.unique(y))

# Printing the accuracy of the classifier
from sklearn.metrics import accuracy_score
print("Accuracy:", accuracy_score(y_test, y_pred))
