from sklearn.datasets import load_iris
from sklearn.feature_selection import RFECV
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold

# Load the dataset
data = load_iris()
X = data.data
y = data.target

# Define the estimator
estimator = SVC(kernel="linear")

# Define the cross-validation method
cv = StratifiedKFold(n_splits=5)

# Configure RFECV to use cross-validation
selector = RFECV(estimator, step=1, cv=cv, scoring='accuracy')

# Fit the model and perform feature selection
selector.fit(X, y)

# Print the results
print("Optimal number of features: %d" % selector.n_features_)
print("Selected features indices: %s" % selector.support_)
print("Feature ranking: %s" % selector.ranking_)
