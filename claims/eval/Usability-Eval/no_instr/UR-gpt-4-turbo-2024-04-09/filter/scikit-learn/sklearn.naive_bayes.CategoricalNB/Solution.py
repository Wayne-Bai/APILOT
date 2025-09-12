from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example data: features and labels
X = [[0, 0], [1, 1], [0, 1], [1, 0]]  # categorical features
y = [0, 1, 0, 1]  # classes or labels

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Initializing the Naive Bayes classifier for categorical features
model = CategoricalNB()

# Training the model
model.fit(X_train, y_train)

# Predicting the labels for test data
predictions = model.predict(X_test)

# Calculating the accuracy of the prediction
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")
