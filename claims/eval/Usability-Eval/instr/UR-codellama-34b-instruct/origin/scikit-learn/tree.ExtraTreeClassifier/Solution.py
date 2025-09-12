
from sklearn.ensemble import RandomForestClassifier

# Load your dataset
X, y = ... # Your data and target variables

# Initialize the classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
clf.fit(X, y)

# Make predictions on new data
predictions = clf.predict(new_data)
