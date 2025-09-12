from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.tree import DecisionTreeClassifier

# Example dataset
from sklearn.datasets import load_iris

# Load data
data = load_iris()
X = data.data
y = data.target

# Create a decision tree classifier
classifier = DecisionTreeClassifier()

# Create the RFECV object with StratifiedKFold cross-validator
rfecv = RFECV(estimator=classifier, step=1, cv=StratifiedKFold(5), scoring='accuracy')

# Fit RFECV
rfecv.fit(X, y)

print("Optimal number of features : %d" % rfecv.n_features_)

# Print support and ranking of features
print("Mask of selected features:", rfecv.support_)
print("Feature ranking:", rfecv.ranking_)
