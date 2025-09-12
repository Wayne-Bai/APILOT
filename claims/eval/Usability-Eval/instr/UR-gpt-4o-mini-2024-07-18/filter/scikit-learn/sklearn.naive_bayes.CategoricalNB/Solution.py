from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
import pandas as pd

# Example dataset
data = pd.DataFrame({
    'feature1': ['A', 'B', 'A', 'C', 'B'],
    'feature2': ['X', 'Y', 'Y', 'X', 'X'],
    'target': [0, 1, 0, 1, 1]
})

# Split the dataset into features and target variable
X = data[['feature1', 'feature2']]
y = data['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with OneHotEncoder and CategoricalNB
model = make_pipeline(OneHotEncoder(), CategoricalNB())

# Fit the model
model.fit(X_train, y_train)

# Example prediction
predictions = model.predict(X_test)

print(predictions)
