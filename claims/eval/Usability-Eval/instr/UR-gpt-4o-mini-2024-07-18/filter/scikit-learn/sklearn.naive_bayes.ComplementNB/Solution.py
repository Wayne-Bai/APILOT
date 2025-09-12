from sklearn.naive_bayes import ComplementNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

# Sample data
documents = [
    'I love programming in Python',
    'Python is great for data science',
    'I enjoy learning new programming languages',
    'Data science is an exciting field',
    'Machine learning is a part of data science',
    'Python can be used for web development'
]
labels = [1, 1, 1, 0, 0, 0]  # 1 for data-related, 0 for others

# Prepare the data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
y = labels

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Complement Naive Bayes classifier
model = ComplementNB()

# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = metrics.accuracy_score(y_test, y_pred)
classification_report = metrics.classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{classification_report}')
