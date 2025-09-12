from sklearn.feature_selection import RFECV
from sklearn.svm import SVC
from sklearn.datasets import make_classification

# Create a randomized dataset
X, y = make_classification(n_samples=1000, n_features=500,
                           n_informative=200, n_redundant=0,
                           random_state=0, shuffle=False)

# Create the RFE object and rank each pixel
svc = SVC(kernel="linear")
rfe = RFECV(estimator=svc, step=1, cv=5, scoring='accuracy')
rfe.fit(X, y)
print("Optimal number of features : %d" % rfe.n_features_)

# Plot number of features VS. cross-validation scores
import matplotlib.pyplot as plt
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classification)")
plt.plot(range(1, len(rfe.grid_scores_) + 1), rfe.grid_scores_)
plt.show()
