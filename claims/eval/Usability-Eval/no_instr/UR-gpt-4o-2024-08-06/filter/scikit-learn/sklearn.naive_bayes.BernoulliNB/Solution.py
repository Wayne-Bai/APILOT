from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset which has binary features and a binary target
# Here we use a toy example with binary features
X = [[1, 0, 1, 0],
     [1, 1, 0, 0],
     [0, 0, 1, 1],
     [0, 1, 0, 1],
     [1, 0, 1, 1]]

y = [0, 1, 0, 1, 0]

# Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Bernoulli Naive Bayes model
model = BernoulliNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy of the classifier
print(f'Accuracy: {accuracy:.2f}')
