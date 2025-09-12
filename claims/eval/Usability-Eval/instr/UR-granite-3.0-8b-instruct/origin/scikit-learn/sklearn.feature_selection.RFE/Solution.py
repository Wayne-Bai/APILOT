from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load iris dataset as an example
iris = load_iris()
X = iris.data
y = iris.target

# Create a RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=0)

# Create a RFE object and rank each feature
rfe = RFE(estimator=clf, n_features_to_select=1)
rfe = rfe.fit(X, y)

# Print the ranking of features
print("Num Features: %d" % (rfe.n_features_))
print("Selected Features: %s" % (rfe.support_))
print("Feature Ranking: %s" % (rfe.ranking_))
