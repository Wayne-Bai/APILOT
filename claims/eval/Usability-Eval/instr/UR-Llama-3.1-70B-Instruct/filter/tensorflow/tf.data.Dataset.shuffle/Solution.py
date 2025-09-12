# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create a sample dataset
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create a TensorFlow dataset from the sample data
dataset = tf.data.Dataset.from_tensor_slices(data)

# Shuffle the dataset
batch_size = 5
shuffle_buffer_size = 10
shuffled_dataset = dataset.shuffle(buffer_size=shuffle_buffer_size).batch(batch_size)

# Print the shuffled dataset
for batch in shuffled_dataset:
    print(batch)
