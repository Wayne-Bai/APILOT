
# Importing scikit-learn
from sklearn.tree import DecisionTreeClassifier

# Creating a Decision Tree Classifier
class MyDecisionTree:
    def __init__(self):
        self.tree = None

    def fit(self, X, y):
        self.tree = self._build_tree(X, y)

    def _build_tree(self, X, y):
        # Implement your own decision tree building algorithm here
        pass

# Usage Example
X = [[0, 0], [1, 1]]
y = [0, 1]

dt = MyDecisionTree()
dt.fit(X, y)
