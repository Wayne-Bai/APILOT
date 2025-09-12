from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification
from sklearn.svm import SVR

# Generate a random n-class classification problem
X, y = make_classification(n_samples=1000, n_features=25, n_informative=3,
                           n_redundant=2, n_classes=4,
                           flip_y=0.01, random_state=1)

# Use the rbf kernel
svm = SVR(kernel='rbf')

# Create the RFE object and rank each feature
rfecv = RFECV(estimator=svm, scoring='accuracy')
rfecv.fit(X, y)

print("Optimal number of features: %d" % rfecv.n_features_)

# Plot number of features VS. cross-validation scores
import matplotlib.pyplot as plt
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score")
plt.plot(range(1, len(rfecv.cv_results_['mean_test_score']) + 1), rfecv.cv_results_['mean_test_score'])
plt.show()
