from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier

# Initialize the gradient boosting classifier
gb_classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3)

# Define the decision tree classifier
tree_classifier = DecisionTreeClassifier(criterion='entropy')

# Initialize the histogram-based gradient boosting classifier
hist_gb_classifier = HistogramGradientBoostingClassifier(base_estimator=tree_classifier, n_estimators=100)
