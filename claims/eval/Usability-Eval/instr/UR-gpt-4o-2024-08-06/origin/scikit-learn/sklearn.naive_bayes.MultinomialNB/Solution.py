# Import necessary libraries from scikit-learn
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example dataset
# X contains feature vectors, y contains labels
# Here we have 6 samples with 3 features each as an example
X = [[2, 1, 0], [1, 0, 1], [3, 3, 0], [1, 1, 1], [0, 2, 2], [0, 1, 3]]
y = [0, 0, 1, 1, 0, 1]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Instantiate the MultinomialNB classifier
model = MultinomialNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
