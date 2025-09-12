# Import the necessary libraries
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Assume you have X (features) and y (labels)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create the Extra Trees Classifier
clf = ExtraTreesClassifier(n_estimators=100, random_state=42)

# Train the Classifier to take the training features and learn how they relate to the training y (the species)
clf.fit(X_train, y_train)

# Apply the Classifier we trained to the test data
y_pred = clf.predict(X_test)

# Compare actual response values (y_test) with predicted response values (y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
