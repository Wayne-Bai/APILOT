# Importing necessary libraries from scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Step 1: Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Step 2: Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Initialize a Logistic Regression classifier
classifier = LogisticRegression(max_iter=1000)

# Step 4: Initialize Recursive Feature Elimination with the chosen classifier
rfe = RFE(estimator=classifier, n_features_to_select=2, step=1)

# Step 5: Perform feature selection
rfe.fit(X_train, y_train)

# Step 6: Get the selected features
selected_features = rfe.support_

# Step 7: Transform the dataset using the selected features
X_train_selected = X_train[:, selected_features]
X_test_selected = X_test[:, selected_features]

# Step 8: Train a new Logistic Regression classifier on the selected features
classifier.fit(X_train_selected, y_train)

# Step 9: Predict the test set output
y_pred = classifier.predict(X_test_selected)

# Step 10: Evaluate the performance of the classifier on the test set
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
