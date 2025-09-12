# Importing the GaussianNB module from scikit-learn
from sklearn.naive_bayes import GaussianNB

# Example data: features and targets
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 1]

# Initializing the GaussianNB model
model = GaussianNB()

# Incremental updates using partial_fit
# Specify all potential classes upfront using classes parameter
classes = np.unique(y)
model.partial_fit(X, y, classes=classes)

# Example of updating the model with new data
new_X = [[3, 2]]
new_y = [1]
model.partial_fit(new_X, new_y)

# Using the model to predict a new value
predicted = model.predict([[2, 0]])
print(predicted)  # Output prediction
