Python
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB

# assuming that our feature data X and target data y are defined
X = ...
y = ...

# initialize the encoder for converting categorical data to numerical
encoder = LabelEncoder()

# apply the encoder to each categorical feature column in X
for i in range(X.shape[1]):
    if X[:, i].dtype == 'object':
        X[:, i] = encoder.fit_transform(X[:, i])

# initialize the model
model = CategoricalNB()

# fit the model on the input data
model.fit(X, y)
