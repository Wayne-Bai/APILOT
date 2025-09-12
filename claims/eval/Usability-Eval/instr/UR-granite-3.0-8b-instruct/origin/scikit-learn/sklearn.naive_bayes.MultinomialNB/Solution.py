from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

# Assuming you have a DataFrame `df` with 'text' and 'label' columns
# 'text' contains the text data and 'label' contains the corresponding labels

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the vectorizer on the 'text' column
X = vectorizer.fit_transform(df['text'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, df['label'], test_size=0.2, random_state=42)

# Initialize the Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Fit the classifier on the training data
clf.fit(X_train, y_train)

# Predict the labels for the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')
