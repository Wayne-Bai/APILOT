# Import necessary libraries
import numpy as np
import tensorflow as tf

# Generate some sample data (replace with your actual data)
np.random.seed(0)
data = np.arange(10)
target = np.random.randint(0, 2, size=(10))

# Verify the data before shuffling
print("Original data:")
print(data)
print("Original target:")
print(target)

# Convert data and target to tensorflow tensors
data_tensor = tf.cast(data, tf.int64)
target_tensor = tf.cast(target, tf.int64)

# Use tf.random.shuffle() function to randomly shuffle the data
shuffled_data, shuffled_target = tf.random.shuffle(data_tensor, target_tensor), tf.random.shuffle(target_tensor)

# Verify the shuffled data
print("\nShuffled data:")
print(shuffled_data)
print("Shuffled target:")
print(shuffled_target)
