from sklearn.datasets import make_classification
from sklearn.feature_selection import RFE
from sklearn.svm import SVC

# Generate a random classification problem
X, y = make_classification(n_samples=1000, n_features=10,
 n_informative=3, n_redundant=0,
 random_state=0, shuffle=False)

# Create a support vector classifier
clf = SVC(kernel="linear", C=1)

# Create the RFE object and rank each pixel
rfe = RFE(estimator=clf, n_features_to_select=1, step=1)
rfe.fit(X, y)

# Print the ranking of features
print(rfe.ranking_)
