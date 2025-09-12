from sklearn.ensemble import ExtraTreesClassifier

# Assuming you have features in 'X' and labels in 'y'
# Replace 'X' and 'y' with your actual data
X = [[...], [...], ...]  # Your feature matrix
y = [...]                 # Your labels

# Initialize the ExtraTreesClassifier
ext_tree_classifier = ExtraTreesClassifier(random_state=42)

# Fit the model
ext_tree_classifier.fit(X, y)

# Predict labels for new data
new_data = [[...]]  # Replace with your new data
predictions = ext_tree_classifier.predict(new_data)

print(predictions)
