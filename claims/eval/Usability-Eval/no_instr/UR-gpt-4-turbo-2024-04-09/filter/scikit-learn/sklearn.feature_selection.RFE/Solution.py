from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load example data
iris = load_iris()
X = iris.data
y = iris.target

# Create a random forest classifier
model = RandomForestClassifier()

# Create the RFE (Recursive Feature Elimination) model
rfe = RFE(estimator=model, n_features_to_select=2)

# Fit the RFE model on the dataset
rfe.fit(X, y)

# Print ranking of features
print("Ranking of features:", rfe.ranking_)
