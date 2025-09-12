from sklearn.feature_selection import RFE
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create a logistic regression model
model = LogisticRegression()

# Perform RFE with a certain number of features
rfe = RFE(model, n_features_to_select=2)

# Fit the model to the data
rfe = rfe.fit(X_train, y_train)

# Print the selected features
print("Selected features:", rfe.support_)
print("Feature rankings:", rfe.ranking_)
