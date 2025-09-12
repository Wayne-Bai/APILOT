# Importing necessary libraries
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Loading the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Creating a Logistic Regression model
model = LogisticRegression(max_iter=2000)

# Creating an instance of Recursive Feature Elimination
rfe = RFE(model, n_features_to_select=2)

# Fitting the RFE instance to the dataset
rfe.fit(X, y)

# Getting the support from the RFE instance
support = rfe.support_

# Using the support to get the ranked features
ranked_features = X.columns[support]

print("Ranked Features:", ranked_features)

# Selecting the top n features and creating a new dataset
n = 2
selected_features = ranked_features[:n]
X_selected = X.loc[:, selected_features]
y_selected = y

# Training a model on the new dataset and evaluating its performance
model.fit(X_selected, y_selected)
y_pred = model.predict(X_selected)
print("Accuracy:", accuracy_score(y_selected, y_pred))
