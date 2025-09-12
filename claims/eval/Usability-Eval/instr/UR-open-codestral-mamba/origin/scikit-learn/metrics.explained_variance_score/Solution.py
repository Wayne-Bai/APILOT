# Importing the required libraries from scikit-learn
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score

# Loading the boston dataset
boston_dataset = load_boston()

# Creating the training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(
    boston_dataset.data, boston_dataset.target, test_size=0.2, random_state=42)

# Creating a linear regression model
model = LinearRegression()

# Training the model
model.fit(X_train, Y_train)

# Making predictions using the test set
predictions = model.predict(X_test)

# Calculating the explained variance score
explained_variance = explained_variance_score(Y_test, predictions)
print('Explained Variance Score:', explained_variance)
