from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
import numpy as np

# Example categorical dataset
data = np.array([
    ['Red', 'Sports', 'Domestic'],
    ['Blue', 'SUV', 'Imported'],
    ['Green', 'SUV', 'Imported'],
    ['Red', 'SUV', 'Domestic'],
    ['Red', 'Sports', 'Imported'],
])

# Corresponding class labels for the examples
labels = np.array(['Yes', 'No', 'Yes', 'No', 'Yes'])

# Encode categorical features
le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()

data_encoded = np.array([
    le1.fit_transform(data[:, 0]),
    le2.fit_transform(data[:, 1]),
    le3.fit_transform(data[:, 2])
]).T

# Instantiate the classifier
model = MultinomialNB()

# Train the model
model.fit(data_encoded, labels)

# New data to predict
new_data = np.array([['Red', 'Sports', 'Domestic']])

# Encode new data
new_data_encoded = np.array([
    le1.transform(new_data[:, 0]),
    le2.transform(new_data[:, 1]),
    le3.transform(new_data[:, 2])
]).T

# Predict
predictions = model.predict(new_data_encoded)
print(predictions)
