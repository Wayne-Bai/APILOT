
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Load your dataset into a Pandas DataFrame
df = pd.read_csv('your_data.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['feature1'], df['feature2'], test_size=0.2)

# Create a MultinomialNB classifier object
clf = MultinomialNB()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Predict the labels of the testing data
predictions = clf.predict(X_test)

# Print the accuracy score
print("Accuracy:", accuracy_score(y_test, predictions))
