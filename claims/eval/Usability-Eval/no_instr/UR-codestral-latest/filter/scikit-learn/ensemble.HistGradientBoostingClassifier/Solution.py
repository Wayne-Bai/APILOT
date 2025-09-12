from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Create a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=42)

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a histogram-based gradient boosting classification tree
clf = HistGradientBoostingClassifier(random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Evaluate the classifier
score = clf.score(X_test, y_test)
print("Test set accuracy: {:.2f}".format(score))
