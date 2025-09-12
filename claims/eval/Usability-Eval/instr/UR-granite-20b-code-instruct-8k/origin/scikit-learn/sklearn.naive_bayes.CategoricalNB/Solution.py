import numpy as np
from sklearn.naive_bayes import CategoricalNB
# Create example data
X = np.array([['male', 'European', 'blue', 'sbinormal', 'short'],
              ['female', 'European', 'blue', 'tall', 'long'],
              ['female', 'African', 'blue', 'short', 'long'],
              ['male', 'African', 'blue', 'tall', 'long'],
              ['male', 'European', 'blue', 'short', 'long'],
              ['female', 'European', 'blue', 'tall', 'long'],
              ['female', 'African', 'yellow', 'short', 'long'],
              ['male', 'African', 'yellow', 'tall', 'long'],
              ['male', 'European', 'yellow', 'short', 'long'],
              ['female', 'European', 'yellow', 'tall', 'long']])
y = np.array(['0', '0', '0', '0', '0', '0', '1', '1', '1', '1'])
# Create and fit the model
model = CategoricalNB()
model.fit(X, y)
# Make a prediction
new_observation = np.array([['female', 'African', 'yellow', 'short', 'long']])
prediction = model.predict(new_observation)
print(prediction)
