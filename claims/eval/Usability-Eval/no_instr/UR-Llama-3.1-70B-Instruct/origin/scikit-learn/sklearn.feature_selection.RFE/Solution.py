# Import necessary libraries
from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFECV
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

# Create a regression dataset
X, y = make_friedman1(n_samples=50, n_features=10, random_state=0)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

# Create an estimator and fit the data
estimator = SVR(kernel="linear")
selector = RFECV(estimator, step=1, cv=5)
selector = selector.fit(X_train, y_train)

# Print the support, ranking and optimal number of features
print("Support:", selector.support_)
print("Feature ranking:", selector.ranking_)
print("Optimal number of features:", selector.n_features_)

# Print the scores of the left-out data
print("Scores of the left-out data: ", selector.grid_scores_)
