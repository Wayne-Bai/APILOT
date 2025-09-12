import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer
from sklearn.metrics import accuracy_score

# Sample binary data
X = np.array([[1, 0, 1, 0],
              [0, 1, 0, 1],
              [1, 1, 1, 0],
              [0, 0, 0, 1],
              [1, 1, 0, 0],
              [0, 1, 1, 1]])

# Sample class labels
y = np.array([0, 1, 0, 1, 0, 1])

# Binzarize the data
binarizer = Binarizer()
X_binarized = binarizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_binarized, y, test_size=0.2, random_state=42)

# Initialize MultinomialNB - close to BernoulliNB with binary counts
model = MultinomialNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
