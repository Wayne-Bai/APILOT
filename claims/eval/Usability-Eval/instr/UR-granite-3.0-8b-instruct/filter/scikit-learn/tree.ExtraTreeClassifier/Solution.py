from sklearn.ensemble import ExtremelyRandomizedTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Assuming X is your features and y is your target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Extremely Randomized Tree Classifier
ert = ExtremelyRandomizedTreeClassifier(n_estimators=100, random_state=42)

# Fit the classifier to the training data
ert.fit(X_train, y_train)

# Predict the target variable for the test data
y_pred = ert.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
