from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Load the iris dataset as an example
iris = load_iris()
X = iris.data
y = iris.target

# Create a logistic regression model
model = LogisticRegression()

# Create a recursive feature elimination object with the chosen model
rfe = RFE(estimator=model, n_features_to_select=3)

# Fit the RFE object to the data
rfe = rfe.fit(X, y)

# Print the ranking of features
print("Feature ranking:")
for i, v in enumerate(rfe.ranking_):
    print("Feature {}: {:.4f}".format(i, v))
