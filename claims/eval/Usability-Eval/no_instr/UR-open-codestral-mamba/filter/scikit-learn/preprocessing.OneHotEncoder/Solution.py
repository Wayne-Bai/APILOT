from sklearn.preprocessing import OneHotEncoder
import numpy as np

# create a sample data
data = np.array(['cat', 'dog', 'horse', 'cat', 'dog', 'bird'])

# Instantiate OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# perform one-hot encoding
encoded_data = encoder.fit_transform(data.reshape(-1, 1))

print(encoded_data)
