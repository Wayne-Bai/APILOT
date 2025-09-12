import numpy as np
import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Sample data creation
data = {
    'Feature1': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Feature2': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Target': [0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Preparing data
X = df[['Feature1', 'Feature2']]
y = df['Target']

# Encoding categorical features
X_encoded = pd.get_dummies(X, drop_first=True)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)

# Creating and training the Naive Bayes classifier
model = CategoricalNB()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:\n', report)
