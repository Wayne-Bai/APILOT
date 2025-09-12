from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selector import train_test_split
from sklearn.isotonic import IsotonicRegression

# Load the iris dataset
iris = datasets.load_iris()

# Preprocess the data (will be explained later)
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, random_state=42)

# Logistic Regression with probability
# For probabilistic calibration, the logistic regression model must be run with the probability flag set to true
lr = LogisticRegression(C=0.01, solver='saga', max_iter=200, random_state=42)

lr.fit(X_train, y_train)

# The predict_proba method provides us with the probability estimates of predicting each label
# Call fit() on an isotonic regression model with the predicted probabilities in the X direction and the true labels in the y direction
ir = IsotonicRegression()

ir.fit(lr.predict_proba(X_train)[:, 1], y_train)

# Plotting predictions agains ground truth for the test data
preds = ir.predict(lr.predict_proba(X_test)[:, 1])

preds
