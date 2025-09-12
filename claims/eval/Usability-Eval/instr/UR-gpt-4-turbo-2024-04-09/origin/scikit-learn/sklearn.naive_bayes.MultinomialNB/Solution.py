from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example data - You can replace these with your actual dataset
X = [[0, 1, 0, 1], [1, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]  # Features
y = [0, 1, 1, 0]  # Labels

# Splitting dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing and training the Multinomial Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
