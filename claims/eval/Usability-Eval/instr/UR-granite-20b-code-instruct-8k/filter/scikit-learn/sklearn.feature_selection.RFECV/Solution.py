from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification
from sklearn.svm import SVC

# Generate a random classification dataset
X, y = make_classification(n_samples=1000, n_features=10,
 n_informative=3, n_redundant=0,
 random_state=0, shuffle=False)

# Create a support vector machine classifier
clf = SVC(kernel="linear", C=1)

# Perform recursive feature elimination with cross-validation
rfecv = RFECV(estimator=clf, step=1, cv=5, scoring='accuracy')
rfecv = rfecv.fit(X, y)

print("Optimal number of features: %d" % rfecv.n_features_)
