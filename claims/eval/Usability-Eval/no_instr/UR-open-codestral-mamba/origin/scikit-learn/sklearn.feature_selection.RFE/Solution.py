from sklearn.datasets import make_classification
from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
import matplotlib.pyplot as plt

# Generate a random n-class classification problem
X, y = make_classification(n_samples=1000, n_features=25, n_informative=3,
                           n_redundant=2, n_classes=4, random_state=42)

# Define a SVC object with 'linear' kernel
svc = SVR(kernel="linear")

# Make an RFECV object with base SVC estimator
rfecv = RFECV(estimator=svc, step=1, cv=5)

# Fit data onto the model
rfecv.fit(X, y)

print("Optimal number of features : %d" % rfecv.n_features_)

# Plot number of features VS. cross-validation scores
plt.figure(figsize=(12, 6))
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()
