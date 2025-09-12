from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Generate a sample dataset
X, y = make_classification(n_samples=100, n_features=20, n_informative=10, n_redundant=5, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Create the RFE model and select 10 features
rfe = RFE(estimator=model, n_features_to_select=10)
rfe.fit(X, y)

# Print the ranking of the features
print("Feature Ranking:")
for i in range(X.shape[1]):
    print(f"Feature {i}: Rank {rfe.ranking_[i]}")
