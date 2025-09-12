from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Initialize the RFECV object
rfecv = RFECV(estimator=clf, step=1, cv=5, scoring='accuracy')

# Fit the RFECV object to the training data
rfecv.fit(X_train, y_train)

# Print the optimal number of features
print("Optimal number of features: ", rfecv.n_features_)

# Print the ranking of features
print("Feature ranking: ", rfecv.ranking_)

# Plot the number of features vs. cross-validation scores
import matplotlib.pyplot as plt
plt.figure()
plt.xlabel("Number of features")
plt.ylabel("Cross validation score (accuracy)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()
