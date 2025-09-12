# Importing necessary libraries from scikit-learn
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import numpy as np

# Generate a dataset (you would typically load your dataset here)
np.random.seed(0)
X = np.random.randint(0, 2, size=(100, 10))  # Categorical features
y = np.random.randint(0, 2, size=(100,))  # Target variable

# Define feature names and target variable name
feature_names = ['feature_' + str(i) for i in range(1, 11)]
target_name = 'target'

# Create a DataFrame
df = pd.DataFrame(X, columns=feature_names)
df[target_name] = y

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[feature_names], df[target_name], test_size=0.2, random_state=42)

# Create a Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.3f}')

print('Classification Report:')
print(classification_report(y_test, y_pred))

print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))
