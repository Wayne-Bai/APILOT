# Import necessary libraries from scikit-learn
from sklearn.feature_selection import RFE
from sklearn.svm import SVC
from sklearn.datasets import load_iris

# Load the iris dataset
data = load_iris()
X = data.data
y = data.target

# Create the RFE (Recursive Feature Elimination) object
estimator = SVC(kernel="linear")
selector = RFE(estimator, n_features_to_select=2, step=1)

# Fit the RFE selector to the data
selector = selector.fit(X, y)

# Output the ranking of the features
print("Ranking of features:", selector.ranking_)
