from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

# Sample data
X = [
    "I love programming and coding",
    "Python is a great language",
    "I enjoy learning new things",
    "Programming is fun",
    "Coding challenges are exciting",
    "I hate bugs in code"
]
y = [1, 1, 1, 1, 1, 0]  # 1 for positive sentiment, 0 for negative sentiment

# Splitting the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a pipeline with CountVectorizer and MultinomialNB
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Training the model
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# Output the predictions
print(predictions)
