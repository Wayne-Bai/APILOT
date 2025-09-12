
from sklearn.datasets import make_classification
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import SelectFromModel

# Create a sample dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_classes=2, random_state=42)

# Train a gradient boosting classifier
clf = GradientBoostingClassifier(random_state=42)
clf.fit(X, y)

# Create a meta-transformer for feature selection based on importance weights
class FeatureSelectorTransformer:
    def __init__(self, clf):
        self.clf = clf
    
    def fit(self, X, y):
        self.clf.fit(X, y)
    
    def transform(self, X):
        return X[:, self.clf.feature_importances_.argsort()[::-1][:5]]

# Apply the meta-transformer for feature selection
feature_selector = FeatureSelectorTransformer(clf)
X_selected = feature_selector.transform(X)
