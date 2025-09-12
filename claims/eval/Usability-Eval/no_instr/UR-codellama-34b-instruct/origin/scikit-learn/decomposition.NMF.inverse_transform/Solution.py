
from sklearn.preprocessing import InverseTransformer
import numpy as np

# Load your data into a numpy array
data = np.load('your_data.npy')

# Create an instance of the inverse transformer class
it = InverseTransformer()

# Fit the inverse transformer to your data
it.fit(data)

# Transform the data back to its original space
original_data = it.transform(data)
