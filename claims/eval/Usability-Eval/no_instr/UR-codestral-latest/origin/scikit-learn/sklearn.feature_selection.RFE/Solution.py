from sklearn.datasets import make_classification
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Generate dummy dataset
X, y = make_classification(n_features=20, n_redundant=5, random_state=1)

# Create a logistic regression model
model = LogisticRegression()

# Define the RFE object
rfe = RFE(model, n_features_to_select=5)

# Fit the data on model
rfe = rfe.fit(X, y)

# Get ranked features
ranking = rfe.ranking_

# Print ranking of features
print(ranking)
