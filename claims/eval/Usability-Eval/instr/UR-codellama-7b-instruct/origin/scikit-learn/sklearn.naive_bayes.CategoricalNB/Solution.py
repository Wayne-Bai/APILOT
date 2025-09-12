
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Load the data
df = pd.read_csv('data.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Initialize the Naive Bayes classifier
nb = MultinomialNB()

# Train the model on the training data
nb.fit(X_train, y_train)

# Evaluate the model on the testing data
y_pred = nb.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
