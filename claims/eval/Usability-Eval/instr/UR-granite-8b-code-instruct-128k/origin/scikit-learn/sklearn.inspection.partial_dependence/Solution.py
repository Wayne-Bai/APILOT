from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_hastie_10_2
from sklearn.inspection import PartialDependenceDisplay

# Load the dataset
X, y = make_hastie_10_2(n_samples=1000, random_state=42)

# Train a random forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X, y)

# Create a PartialDependenceDisplay object
display = PartialDependenceDisplay.from_estimator(
    clf, X, ["feature0", "feature1"], grid_resolution=10
)

# Plot the partial dependence
display.plot()
