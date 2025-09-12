from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Create a logistic regression model
model = LogisticRegression(max_iter=200)

# Initialize Recursive Feature Elimination with the model and specify the number of features to select
rfe = RFE(estimator=model, n_features_to_select=2)

# Fit RFE
rfe.fit(X, y)

# Get the ranking of features
ranking = rfe.ranking_

# Output the rankings
for i, rank in enumerate(ranking):
    print(f"Feature {i+1}: Rank {rank}")
