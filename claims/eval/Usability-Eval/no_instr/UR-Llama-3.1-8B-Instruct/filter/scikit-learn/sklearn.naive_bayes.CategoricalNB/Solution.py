# Import necessary libraries from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Import pandas library to handle data
import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = {
    'Feature1': np.random.choice(['Cat', 'Dog', 'Bird'], 100),
    'Feature2': np.random.choice(['Male', 'Female'], 100),
    'Feature3': np.random.choice(['Old', 'Young'], 100),
    'Target': np.random.randint(0, 2, 100)  # Binary classification
}
df = pd.DataFrame(data)

# Encode categorical features using LabelEncoder
encoder = LabelEncoder()
for column in ['Feature1', 'Feature2', 'Feature3']:
    df[column] = encoder.fit_transform(df[column])

# Split dataset into features (X) and target (y)
X = df.drop('Target', axis=1)
y = df['Target']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Train the model
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
