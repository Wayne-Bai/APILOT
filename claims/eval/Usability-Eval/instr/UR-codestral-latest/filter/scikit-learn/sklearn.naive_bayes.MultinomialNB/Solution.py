# Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Assume we have the following dummy data
text = ['I love machine learning', 'I love coding', 'Machine learning is a part of deep learning', 'I love python and coding', 'Coding is easy with python']
labels = ['Machine Learning', 'Coding', 'Machine Learning', 'Coding', 'Coding']

# Preprocess the text data using CountVectorizer
cv = CountVectorizer()
features = cv.fit_transform(text)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Create a Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Train the classifier using the training data
clf.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = clf.predict(X_test)

# Print the predictions
print(y_pred)
