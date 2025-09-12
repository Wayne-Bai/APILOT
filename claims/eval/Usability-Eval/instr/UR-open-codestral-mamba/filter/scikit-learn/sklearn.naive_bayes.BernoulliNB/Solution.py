from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB

# Sample data
X = ['Hello, how are you?', 'Win money, win from home.', 'Call me now.', 'Hello, call hello you tomorrow?']
y = ['pos', 'neg', 'neg', 'pos']

# Convert text into a matrix of token counts
vector = CountVectorizer(binary='true')
X = vector.fit_transform(X)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create Bernoulli Naive Bayes classifier
nb = BernoulliNB()

# Train the classifier
nb.fit(X_train.toarray(), y_train)

# Test the classifier
y_pred = nb.predict(X_test.toarray())

# Print predictions
print("Predictions: ", y_pred)
