from sklearn.base import BaseEstimator, ClassifierMixin

# Custom Estimator
class CustomClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, param1=None, param2=None):
        self.param1 = param1
        self.param2 = param2

    def fit(self, X, y):
        # Here we should define the fit method to fit the data
        self.X_ = X
        self.y_ = y
        return self

    def predict(self, X):
        # Here we should define the predict method to predict on data
        return (self.X_ * self.param1 + self.y_ * self.param2) % 2

# Test the custom estimator
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Create a toy dataset
X, y = make_classification(n_samples=1000, n_features=20,random_state=42)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the custom classifier
custom_clf = CustomClassifier(param1=0.5, param2=0.2)

# Fit the classifier
custom_clf.fit(X_train, y_train)

# Predict
y_pred = custom_clf.predict(X_test)

# Check if it adheres to scikit-learn conventions
try:
    from sklearn.utils.validation import check_is_fitted
    check_is_fitted(custom_clf)
    print("The custom estimator adheres to scikit-learn conventions.")
except ImportError:
    print("Check_is_fitted is not available in the version of scikit-learn used.")

