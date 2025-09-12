from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.inspection import plot_partial_dependence
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Plot partial dependence plots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

for i, feature in enumerate(iris.feature_names):
    plot_partial_dependence(clf, X_train, [feature], ax=axs[i], n_jobs=1)

plt.show()
