from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import RFECV

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a model
model = DecisionTreeClassifier()

# Recursive Feature Elimination with Cross-Validation
selector = RFECV(estimator=model, step=1, cv=5)
selector.fit(X_train, y_train)

# Print the selected features
print("Optimal number of features:", selector.n_features_)
print("Selected features:", selector.support_)
print("Feature ranking:", selector.ranking_)
