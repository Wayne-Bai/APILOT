from sklearn.utils import estimator_checks
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Load sample data
data = load_iris()
X, y = data.data, data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the LogisticRegression estimator
estimator = LogisticRegression(max_iter=200)

# Check the estimator
estimator_checks.check_estimator(estimator)
