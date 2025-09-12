
# Import necessary libraries
from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification
from sklearn.svm import SVR
from sklearn.model_selection import StratifiedKFold

# Generate a random n-class classification problem
X, y = make_classification(n_samples=1000, n_features=25, n_informative=3,
                           n_redundant=2, n_classes=4, random_state=0,
                           shuffle=False)

# Create a SVM with linear kernel
svc = SVR(kernel="linear")

# Create the RFECV object
rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(10), scoring='accuracy')

# Fit the RFECV object to the data
rfecv.fit(X, y)

# Display the optimal number of features
print(f"Optimal number of features is {rfecv.n_features_}")

# Mask the features that have been selected
selected_features = X[:, rfecv.support_]

# Print out the selected features
print("Selected features:", selected_features)

