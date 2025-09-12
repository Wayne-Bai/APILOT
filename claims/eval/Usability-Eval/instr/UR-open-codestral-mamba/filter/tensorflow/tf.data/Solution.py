import tensorflow as tf
import numpy as np

# Generate some random data
data = np.random.rand(100, 10)

# Convert the NumPy array to TensorFlow's Dataset object
dataset = tf.data.Dataset.from_tensor_slices(data)

# Shuffle the dataset
shuffled_dataset = dataset.shuffle(buffer_size=100)

# Convert the shuffled Dataset object back to NumPy array
shuffled_data = np.array(list(shuffled_dataset))

print(shuffled_data)
