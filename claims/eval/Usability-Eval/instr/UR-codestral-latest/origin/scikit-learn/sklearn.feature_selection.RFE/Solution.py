from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Create a sample classification dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)

# Define the logistic regression estimator
model = LogisticRegression(solver='lbfgs', max_iter=10000)

# Define the RFE model
rfe = RFE(model, n_features_to_select=2)

# Fit the RFE model on the data
fit = rfe.fit(X, y)

# Print the feature ranking
print("Feature Ranking: ", fit.ranking_)
