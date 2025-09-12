from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Generate a random binary classification problem
X, y = make_classification(n_samples=1000, n_features=500,
                           n_informative=100, n_redundant=0,
                           random_state=0, shuffle=False)

# Create the RFE object and rank the features
svc = LogisticRegression(solver='liblinear')
rfe = RFECV(estimator=svc, step=1, cv=5, scoring='accuracy')
rfe.fit(X, y)

# Print the number of selected features
print("Num Features: %d" % rfe.n_features_)
