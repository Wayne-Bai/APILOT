from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example dataset with categorical features
X = [
    [1, 2, 3],
    [1, 0, 1],
    [0, 2, 0],
    [1, 0, 3],
    [0, 1, 1]
]

y = [0, 1, 0, 1, 0]  # Example target values

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the CategoricalNB classifier
model = CategoricalNB()

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict the labels for the test data
y_pred = model.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")
