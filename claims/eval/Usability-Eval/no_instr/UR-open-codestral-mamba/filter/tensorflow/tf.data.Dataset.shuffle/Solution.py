import tensorflow as tf
import numpy as np

# Create a 2D tensor with random values
input_data = np.random.rand(10, 5)

# Convert the numpy array to a tensor
input_tensor = tf.convert_to_tensor(input_data, dtype=tf.float32)

# Shuffle the tensor along the first dimension
shuffled_tensor = tf.random.shuffle(input_tensor, seed=None)

# Convert the tensor back to a numpy array
shuffled_data = shuffled_tensor.numpy()

# Print the shuffled data
print(shuffled_data)
