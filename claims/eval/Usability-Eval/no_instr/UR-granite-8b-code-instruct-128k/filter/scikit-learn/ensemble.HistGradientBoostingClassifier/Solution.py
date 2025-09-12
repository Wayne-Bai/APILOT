
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import HistogramEncoder

# Load data
X, y = load_data()

# Encode categorical features
encoder = HistogramEncoder()
X = encoder.fit_transform(X)

# Define gradient boosting classifier
clf = GradientBoostingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

# Fit the model
clf.fit(X, y)
