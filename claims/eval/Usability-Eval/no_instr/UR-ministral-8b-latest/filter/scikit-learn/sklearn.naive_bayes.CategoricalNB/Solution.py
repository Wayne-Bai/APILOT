import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

# Assuming there's a DataFrame named df with 'features' as raw categorical data and 'target' as the target variable
# Example: df = pd.DataFrame({'features': [['a', 'b'], ['b', 'c']], 'target': [0, 1]})

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['features'], df['target'], test_size=0.2, random_state=42)

# Creating the pipeline and model
pipeline = make_pipeline(
    DictVectorizer(),  # Convert dict data into a matrix
    MultinomialNB()
)

# Training the model
pipeline.fit(X_train, y_train)

# Predicting on the test set
y_pred = pipeline.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)
