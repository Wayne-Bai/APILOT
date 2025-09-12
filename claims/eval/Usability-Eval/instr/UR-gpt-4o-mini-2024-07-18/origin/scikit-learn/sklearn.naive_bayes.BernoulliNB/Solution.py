from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

# Sample data
X = ['spam message one', 'spam message two', 'not spam message one', 'not spam message two']
y = [1, 1, 0, 0]  # 1: spam, 0: not spam

# Convert text data to feature vectors
vectorizer = CountVectorizer(binary=True)
X_vectorized = vectorizer.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.25, random_state=42)

# Initialize the Multinomial Naive Bayes classifier
model = MultinomialNB()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
