# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import classification_report
import pandas as pd

# Let's assume we have a dataset in a DataFrame called df with categorical features and a target variable
# For the purpose of this example, I'll generate some random data with 5 categorical features and a target variable
import random
import string

# Function to generate random categorical data
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Generate random data
data = {
    'feature1': [random_string(5) for _ in range(1000)],
    'feature2': [random_string(5) for _ in range(1000)],
    'feature3': [random_string(5) for _ in range(1000)],
    'feature4': [random_string(5) for _ in range(1000)],
    'feature5': [random_string(5) for _ in range(1000)],
    'target': [random.choice([0, 1]) for _ in range(1000)]
}

df = pd.DataFrame(data)

# Convert categorical data to numbers
le = LabelEncoder()
for column in df.columns:
    df[column] = le.fit_transform(df[column])

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.2, random_state=1)

# Create and train the model
model = CategoricalNB()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Print a classification report
print(classification_report(y_test, predictions))
